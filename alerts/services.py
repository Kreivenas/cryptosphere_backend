import requests
import logging

logger = logging.getLogger(__name__)

class CryptoService:
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_all_prices(coin_ids=['bitcoin', 'ethereum', 'solana']):
        """
        Fetches multiple prices in a single API call.
        """
        url = f"{CryptoService.BASE_URL}/simple/price"
        params = {
            'ids': ','.join(coin_ids),
            'vs_currencies': 'usd'
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Batch price fetch failed: {e}")
            return None