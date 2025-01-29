from django.contrib import admin
from .models import MenuItem, Category

# Register your models here.

class AdminMenu(admin.ModelAdmin):
    list_display = ["name","price"]

class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Category)
admin.site.register(MenuItem)