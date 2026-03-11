import requests
import logging
from .models import Alert

logger = logging.getLogger(__name__)


class CryptoService:
    """
    Service layer to handle external cryptocurrency API interactions.
    Currently using CoinGecko Public API.
    """
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_price(coin_id='bitcoin'):
        """
        Fetches the current price of a coin in USD.
        :param coin_id: The ID of the coin (e.g., 'bitcoin', 'ethereum')
        :return: Decimal price or None if failed
        """
        url = f"{CryptoService.BASE_URL}/simple/price"
        params = {
            'ids': coin_id,
            'vs_currencies': 'usd'
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # Raises error for 4xx or 5xx responses
            data = response.json()

            price = data.get(coin_id, {}).get('usd')
            if price:
                logger.info(f"Successfully fetched price for {coin_id}: ${price}")
                return price

            logger.warning(f"Price for {coin_id} not found in response.")
            return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching price from CoinGecko: {e}")
            return None


def check_all_alerts():
    """
    Core business logic: Iterates through active alerts and
    compares target prices with live market data.
    """
    # 1. We'll check BTC and ETH for now
    currencies_to_check = ['bitcoin', 'ethereum']

    for coin_id in currencies_to_check:
        current_price = CryptoService.get_price(coin_id)

        if not current_price:
            continue

        # Map 'bitcoin' ID to our 'BTC' choice in Model
        symbol = 'BTC' if coin_id == 'bitcoin' else 'ETH'

        # 2. Get all pending alerts for this currency
        active_alerts = Alert.objects.filter(
            is_triggered=False,
            currency=symbol
        )

        for alert in active_alerts:
            # Business Logic: Check if price reached target
            # In a real SaaS, we check both UP and DOWN directions.
            # For now: trigger if current price is >= target
            if current_price >= alert.target_price:
                logger.info(f"!!! TRIGGERED !!! {alert.user.username}'s {symbol} alert at {alert.target_price}")

                # Update status so we don't trigger it again
                alert.is_triggered = True
                alert.save()

                # TODO: Integrated Email/Telegram/SMS service here
            else:
                logger.info(
                    f"Status: {symbol} is ${current_price}. Target {alert.target_price} not reached for {alert.user.username}")