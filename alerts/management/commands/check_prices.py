import logging
from django.core.management.base import BaseCommand
from alerts.services import check_all_alerts

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Custom management command to fetch current crypto prices
    and check them against user-defined alerts.
    Usage: python manage.py check_prices
    """
    help = 'Fetches live prices from CoinGecko and triggers pending alerts'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--- Starting Price Check Cycle ---'))

        try:
            # We call the service logic we wrote earlier
            check_all_alerts()
            self.stdout.write(self.style.SUCCESS('Successfully finished checking all alerts.'))
        except Exception as e:
            logger.error(f"Critical error during price check: {e}")
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))

        self.stdout.write(self.style.SUCCESS('--- Cycle Finished ---'))