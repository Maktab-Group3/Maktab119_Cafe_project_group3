from django.contrib import admin
from .models import MenuItem, Category
# Register your models here.
class AdminMenuItem(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'discount_percentage',
        'description',
        'serving_time_start',
        'serving_time_start',
        'estimated_cooking_time',
        'entity',
        'category',
        'discounted_price',
        'discount_stock',


    ]
    
    
class AdminCategory(admin.ModelAdmin):
    list_display =[
        'name',
    ]
    
    
admin.site.register(MenuItem, AdminMenuItem)  
admin.site.register(Category, AdminCategory)  

