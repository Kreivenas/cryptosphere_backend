from django.db import models
from django.contrib.auth.models import User


class Alert(models.Model):
    """
    Represents a user-defined price alert for a specific cryptocurrency.
    This is the core entity for the SaaS alert system.
    """

    CURRENCY_CHOICES = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('SOL', 'Solana'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='alerts'
    )

    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default='BTC'
    )

    target_price = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    is_triggered = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | {self.currency} at {self.target_price}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Price Alert"
        verbose_name_plural = "Price Alerts"
