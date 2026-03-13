import logging

logger = logging.getLogger(__name__)

class NotificationService:
    """
    Handles all outgoing communications to users.
    Currently supports Console/Logs. Email/Telegram to be added.
    """

    @staticmethod
    def send_price_alert(alert, current_price):
        """
        Dispatches a notification when a price target is met.
        """
        message = (
            f"Subject: 🚀 Crypto Alert for {alert.currency}!\n"
            f"Hello {alert.user.username},\n"
            f"Your target price of ${alert.target_price} for {alert.currency} has been reached.\n"
            f"Current market price: ${current_price}.\n"
            f"Check your dashboard for more details."
        )

        # 1. Log the notification (For internal tracking)
        logger.info(f"DISPATCHING NOTIFICATION to {alert.user.email} for {alert.currency}")

        # 2. Print to console (For development visibility)
        print("\n" + "="*50)
        print(message)
        print("="*50 + "\n")

        # TODO: Integration with SendGrid or AWS SES goes here
        return True