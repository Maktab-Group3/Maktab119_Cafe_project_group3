from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator
# from ordrs.models import Order

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=80,validators= [MinLengthValidator(2)])
    price = models.DecimalField(max_digits=8)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    description = models.TextField()
    serving_time_period = models.TimeField()
    estimated_cooking_time_choices = [
        ('10 min','10 min'),
        ('20 min','20 min'),
        ('30 min','30 min'),
        ]
    estimated_cooking_time = models.CharField(max_length=50, choices=estimated_cooking_time_choices, default='null')
    entity = models.SmallIntegerField()
    category = models.ForeignKey("Category", on_delete= CASCADE)
    # order = models.ManyToManyField(Order)
    
    
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
    