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
    estimated_cooking_time = models.CharField()
    entity = models.SmallIntegerField()
    category = models.ForeignKey("Category", on_delete= CASCADE)
    # order = models.ManyToManyField(Order)
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    