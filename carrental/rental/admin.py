from django.contrib import admin
from .models import Car, Equipment

# Register your models here.
admin.site.register(Car, list_display = (
    'id',
    'brand',
    'model',
    'color', 
    'price', 
    'engine_type', 
    'engine_power', 
    'gearbox_type', 
    'available', 
    'category',
))
admin.site.register(Equipment)
