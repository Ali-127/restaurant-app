from django.contrib import admin
from .models import Menu, MenuItem, Order

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Order)
