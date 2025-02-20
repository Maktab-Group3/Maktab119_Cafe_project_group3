from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.contrib.auth.models import User

# from ordrs.models import Order
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100, default='null' )
    image = models.ImageField(upload_to='uploads/',null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class MenuItem(models.Model):
    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(2)],
        help_text="Name of the menu item (minimum 2 characters).")
    
    price = models.BigIntegerField(
        help_text="Price of the item in decimal format.")
    
    discount_percentage = models.IntegerField(choices=[(0,"0%"),(10,"10%"),(15,"15%"),(20,"20%")], default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    discount_stock = models.IntegerField(default=0)
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
        related_name='menu_items')
    
    image = models.ImageField(upload_to='uploads/',null=True)
    # order = models.ManyToManyField(Order)
    
    def get_duration(self):
        start_delta = timedelta(hours=self.start_time.hour, minutes=self.start_time.minute, seconds=self.start_time.second)
        end_delta = timedelta(hours=self.end_time.hour, minutes=self.end_time.minute, seconds=self.end_time.second)
        duration = (end_delta - start_delta)
        return duration
      
    def reduce_discount_stock(self):
        if self.discount_stock > 0 :
            self.discount_stock -= 1
            if self.discount_stock == 0 :
                self.discount_percentage = 0
                self.apply_discount()
            self.save()  

    def save(self, *args, **kwargs):
        if self.discount_percentage > 0 and int(self.discount_stock) > 0:
            discount_amount = (self.price*self.discount_percentage)/100
            self.discounted_price = self.price - discount_amount
        else :
            self.discounted_price = self.price

        super().save(*args, **kwargs)          
    def __str__(self):
        return f'{self.name, self.price, self.description}'

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE , related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Comment from {self.user.username}: for {self.menu_item.name}"