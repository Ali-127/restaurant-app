from django.contrib import admin
from .models import Reservation
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'time', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['user__username']
    date_hierarchy = 'date'
    ordering = ['-date', '-time']
