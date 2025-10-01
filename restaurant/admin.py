from django.contrib import admin
from .models import Menu, MenuItem, Order, OrderItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu', 'price', 'is_available', 'image']
    list_filter = ['menu', 'is_available']
    search_fields = ['name', 'description']
    list_editable = ['is_available']
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['menu_item', 'quantity', 'price']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'total_amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['order_id', 'user__username']
    readonly_fields = ['order_id', 'created_at']
    inlines = [OrderItemInline]
    ordering = ['-created_at']

