import requests
import logging
from .models import Alert
from .notifications import NotificationService

logger = logging.getLogger(__name__)


class CryptoService:
    """
    Service layer to handle external cryptocurrency API interactions.
    """
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_price(coin_id='bitcoin'):
        url = f"{CryptoService.BASE_URL}/simple/price"
        params = {'ids': coin_id, 'vs_currencies': 'usd'}
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get(coin_id, {}).get('usd')
        except Exception as e:
            logger.error(f"Failed to fetch price for {coin_id}: {e}")
            return None


def check_all_alerts():
    """
    Main engine: evaluates prices and dispatches notifications.
    """
    asset_map = {
        'bitcoin': 'BTC',
        'ethereum': 'ETH',
        'solana': 'SOL'
    }

    print("\n--- [SYSTEM] Starting Price Check Cycle ---")

    for coin_id, symbol in asset_map.items():
        current_price = CryptoService.get_price(coin_id)

        if current_price is None:
            print(f"--- [ERROR] Skipping {symbol}: Price data unavailable")
            continue

        active_alerts = Alert.objects.filter(is_triggered=False, currency=symbol)
        print(f"--- [INFO] Asset: {symbol} | Price: ${current_price} | Active Alerts: {active_alerts.count()}")

        for alert in active_alerts:
            # Trigger logic: Price meets or exceeds target
            if current_price >= alert.target_price:
                print(f"--- [TRIGGER] User: {alert.user.username} | {symbol} target {alert.target_price} reached!")

                # Update DB state
                alert.is_triggered = True
                alert.save()

                # Dispatch notification directly
                NotificationService.send_price_alert(alert, current_price)
            else:
                print(f"--- [PENDING] User: {alert.user.username} | Target: {alert.target_price}")

    print("--- [SYSTEM] Price Check Cycle Finished ---\n")