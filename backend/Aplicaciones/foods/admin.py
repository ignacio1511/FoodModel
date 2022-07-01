from django.contrib import admin

from .models import Food, FoodImageURL

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodImageURL)
