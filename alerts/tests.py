from django.test import TestCase
from django.contrib.auth.models import User
from .models import Alert


class AlertModelTest(TestCase):
    """
    Test suite for the Alert model integrity.
    Ensures that data validation and string representation work as expected.
    """

    def setUp(self):
        """
        Initial setup for test data.
        Creates a test user to associate with alerts.
        """
        self.user = User.objects.create_user(username='testuser', password='securepassword123')

    def test_alert_creation_and_fields(self):
        """
        Verifies that an Alert object is correctly saved with the provided data.
        """
        alert = Alert.objects.create(
            user=self.user,
            currency='BTC',
            target_price=65000.50
        )

        self.assertEqual(alert.currency, 'BTC')
        self.assertEqual(float(alert.target_price), 65000.50)
        self.assertFalse(alert.is_triggered, "New alerts should not be triggered by default.")

    def test_alert_string_representation(self):
        """
        Ensures the __str__ method returns the expected format for Admin UI and logging.
        """
        alert = Alert.objects.create(user=self.user, currency='ETH', target_price=2500.00)
        expected_str = f"{self.user.username} | ETH at 2500.0"
        self.assertEqual(str(alert), expected_str)

    def test_alert_ordering(self):
        """
        Verifies that alerts are ordered by creation date (newest first) as per Meta options.
        """
        Alert.objects.create(user=self.user, currency='BTC', target_price=60000)
        Alert.objects.create(user=self.user, currency='ETH', target_price=3000)

        alerts = Alert.objects.all()
        self.assertEqual(alerts[0].currency, 'ETH')  # Newest first