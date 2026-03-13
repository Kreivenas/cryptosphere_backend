import requests
import logging

logger = logging.getLogger(__name__)


class NotificationService:
    """
    Handles encrypted communication with Telegram Bot API.
    """
    TELEGRAM_TOKEN = "8094124388:AAEtKlBtXowUJ9QdFGzJGd2rX5SfcBuyfH8"

    # Tavo ID jau čia!
    TELEGRAM_CHAT_ID = "1379181051"

    @staticmethod
    def send_telegram_message(message):
        """
        Dispatches a secure message to the specified Telegram Chat ID.
        """
        url = f"https://api.telegram.org/bot{NotificationService.TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": NotificationService.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return True
        except Exception as e:
            logger.error(f"Telegram API dispatch error: {e}")
            return False

    @staticmethod
    def send_price_alert(alert, current_price):
        """
        Formats and sends the high-priority crypto alert.
        """
        message = (
            f"🚀 <b>CRYPTO NOTIFICATION</b> 🚀\n\n"
            f"Asset: <b>{alert.currency}</b>\n"
            f"Status: <b>Target Met</b>\n"
            f"Target Price: <b>${alert.target_price}</b>\n"
            f"Market Price: <b>${current_price}</b>\n\n"
            f"<i>Powered by CryptoSphere Engine v1.0</i>"
        )

        print(f"--- [DISPATCH] Sending Telegram alert to user {alert.user.username}")
        return NotificationService.send_telegram_message(message)