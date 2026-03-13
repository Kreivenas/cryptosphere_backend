from rest_framework import viewsets
from .models import Alert
from .serializers import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    """
    API for managing crypto alerts.
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer