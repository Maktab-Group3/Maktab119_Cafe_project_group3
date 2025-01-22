from django.db import models
from tkinter import CASCADE
from menu_items.models import menu_item
from table.models import table
from user.models import user 
from receipts.models import receipt


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Order(TimeStampedModel):
    
    menu_item = menu_item.models.ForeignKey('menu_item', on_delete=models.CASCADE, name='menu_item')
    table = table.models.ForeignKey('table', on_delete=models.CASCADE, name='table')
    user = user.models.ForeignKey('user', on_delete=models.CASCADE, name='user') #
    recipt= recipt.models.ForeignKey('recipt', on_delete=models.CASCADE, name='recipt')
    number_of_order = models.IntegerField()
    
    payment_status = [
        ('Successful','Successful'),
        ('Pending','Pending'),
        ('Cancelled','Cancelled')
    ]
    payment_status=models.CharField(choices=payment_status ,default=None ,max_length=10)

    status = [
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('In Preparation','In Preparation'),
        ('Delivered','Delivered'),
        ('Canceled','Canceled')
        
    ]
    
   
    take_a_way =models.BooleanField(default= False)

    def __str__(self):
        return f"{self.number},{self.payment_status},{self.status},{self.take_a_way}" # +ForeignKey
        

    
    def __str__(self):
        return f"{self.created_at},{self.updated_at}"

#parsa
class Receipt(TimeStampedModel):
    total_price = models.DecimalField(max_digits=10, decimal_places=5)
    is_refunded = models.BooleanField(default=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.total_price}'
   
  
       
