from celery import shared_task
from .models import Alert
from .services import CryptoService
from .notifications import NotificationService


@shared_task(name='alerts.tasks.check_all_alerts')
def check_all_alerts():
    # Console heartbeat
    print("\n[!] CELERY: STARTING PRICE CHECK...")

    asset_map = {
        'bitcoin': 'BTC',
        'ethereum': 'ETH',
        'solana': 'SOL'
    }

    # Batch fetch prices to avoid 429 errors
    data = CryptoService.get_all_prices(list(asset_map.keys()))

    if not data:
        print("[!] CELERY: API DATA UNAVAILABLE")
        return

    for coin_id, symbol in asset_map.items():
        price = data.get(coin_id, {}).get('usd')
        if price is None:
            continue

        # Fetch only untriggered alerts for this asset
        alerts = Alert.objects.filter(is_triggered=False, currency=symbol)
        print(f"[!] {symbol}: ${price} | Active Alerts: {alerts.count()}")

        for alert in alerts:
            if price >= alert.target_price:
                print(f"[!] TRIGGER: {symbol} target reached for user {alert.user.username}")

                # Execute notification
                NotificationService.send_price_alert(alert, price)

                # Mark as handled
                alert.is_triggered = True
                alert.save()

    print("[!] CELERY: CYCLE FINISHED\n")