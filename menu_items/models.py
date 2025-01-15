from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import timedelta
# from ordrs.models import Order

# Create your models here.

class Category(models.Model):
    name_choices = [('Pastries','Pastries'),
                    ('Brunch','Brunch'),
                    ('Desserts','Desserts'),
                    ('Soups','Soups'),
                    ('Salads','Salads'),
                    ('Appetizers','Appetizers'),
                    ('Specialty Cocktails','Specialty Cocktails'),
                    ('Coffees','Coffees'),
                    ('Teas','Teas')
                    ('Entrees','Entrees'),
                    ('Signature Dishes','Signature Dishes'),
                    ]
    name = models.CharField(max_length=50,choices=name_choices, default='null' )
    
    def __str__(self):
        return f'{self.name}'
    
class MenuItem(models.Model):
    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(2)],
        help_text="Name of the menu item (minimum 2 characters).")
    
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Price of the item in decimal format.")
    
    discount = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Discount as a decimal value (e.g., 0.15 for 15%).")
    
    description = models.TextField(
        blank=True,
        help_text="Detailed description of the menu item.")
    serving_time_start = models.TimeField()
    serving_time_end = models.TimeField()
    estimated_cooking_time_choices = [
        ('10 min','10 min'),
        ('20 min','20 min'),
        ('30 min','30 min'),
        ]
    estimated_cooking_time = models.CharField(
        max_length=50, 
        choices=estimated_cooking_time_choices, 
        default='null',
        help_text="Estimated time to prepare the dish.")
    
    entity = models.SmallIntegerField(
        help_text="Number of items available."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items',
        help_text="Category to which this item belongs.")
    # order = models.ManyToManyField(Order)
    
    def get_duration(self):
        start_delta = timedelta(hours=self.start_time.hour, minutes=self.start_time.minute, seconds=self.start_time.second)
        end_delta = timedelta(hours=self.end_time.hour, minutes=self.end_time.minute, seconds=self.end_time.second)
        return end_delta - start_delta

    def is_duration_exceeding(self, hours):
        """
        بررسی می‌کند که آیا بازه زمانی از مقدار مشخص (به ساعت) بیشتر است یا نه
        """
        duration = self.get_duration()
        return duration > timedelta(hours=hours)
        
    
    def __str__(self):
        return f'{self.name, self.price, self.description}'
    
