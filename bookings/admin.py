from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date', 'status', 'total_price')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('property__title', 'tenant__email', 'notes')
    date_hierarchy = 'created_at' 