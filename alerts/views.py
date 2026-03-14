from rest_framework import viewsets, permissions
from .models import Alert
from .serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing cryptocurrency price alerts.

    Features:
    - Strict object-level permission (users access only their own data).
    - Automatic user assignment during creation.
    - Full CRUD support for authenticated users.
    """
    serializer_class = AlertSerializer

    # Restrict access to authenticated users only
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset to return only alerts owned by the current user.
        Ensures data isolation and security.
        """
        return Alert.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Custom create logic to automatically link the alert to the
        authenticated user, preventing integrity constraint violations.
        """
        serializer.save(user=self.request.user)