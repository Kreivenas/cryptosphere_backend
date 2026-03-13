from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    """
    Standard serializer for Crypto Alert model.
    """
    class Meta:
        model = Alert
        fields = ['id', 'currency', 'target_price', 'created_at', 'is_triggered']
        read_only_fields = ['id', 'created_at', 'is_triggered']