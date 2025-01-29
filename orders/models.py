from django.db import models
from menu_items.models import MenuItem
# from tables.models import Table



class TimeStampeMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# class Order(TimeStampeMixin):
    
#     menu_item = MenuItem.models.ForeignKey('menu_item', on_delete=models.CASCADE, name='menu_item')
#     table = Table.models.ForeignKey('table', on_delete=models.CASCADE, name='table')
#     user = User.models.ForeignKey('user', on_delete=models.CASCADE, name='user') #
# #    recipt= recipt.models.ForeignKey('recipt', on_delete=models.CASCADE, name='recipt')
#     number_of_order = models.IntegerField()
    
#     payment_status = [
#         ('Successful','Successful'),
#         ('Pending','Pending'),
#         ('Cancelled','Cancelled')
#     ]
#     payment_status=models.CharField(choices=payment_status ,default=None ,max_length=10)

#     status = [
#         ('Pending','Pending'),
#         ('Confirmed','Confirmed'),
#         ('In Preparation','In Preparation'),
#         ('Delivered','Delivered'),
#         ('Canceled','Canceled')
        
#     ]
   
#     take_a_way =models.BooleanField(default= False)

#     def __str__(self):
#         return f"{self.number},{self.payment_status},{self.status},{self.take_a_way}" # +ForeignKey
        

    
#     def __str__(self):
#         return f"{self.created_at},{self.updated_at}"



# #this codes belong to the reza

class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} X {self.quantity}"   
    
