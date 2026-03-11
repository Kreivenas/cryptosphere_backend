from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'target_price', 'is_triggered', 'created_at')
    list_filter = ('currency', 'is_triggered')
    search_fields = ('user__username', 'currency')
    readonly_fields = ('created_at', 'updated_at')
