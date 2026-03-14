import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class NotificationService:
    """
    Sutvarkyta klasė pranešimų siuntimui.
    """

    @staticmethod
    def send_telegram_message(message):

        token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)

        if not token or not chat_id:
            logger.error("TELEGRAM_BOT_TOKEN arba TELEGRAM_CHAT_ID nerastas settings.py faile!")
            return False

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return True
        except Exception as e:
            logger.error(f"Telegram siuntimo klaida: {e}")
            return False

    @staticmethod
    def send_price_alert(alert, current_price):

        message = (
            f"🚀 <b>KRIPTO ALERTAS!</b>\n\n"
            f"Turtas: <b>{alert.currency}</b>\n"
            f"Target kaina: ${alert.target_price}\n"
            f"Dabartinė kaina: <b>${current_price}</b>\n\n"
            f"Vartotojas: {alert.user.username}"
        )

        return NotificationService.send_telegram_message(message)