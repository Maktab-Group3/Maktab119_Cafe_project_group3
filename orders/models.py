from django.db import models
from menu_items.models import MenuItem
from tables.models import Table
# from tables.models import Table



class TimeStampeMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Order(TimeStampeMixin):

    menu_items = models.ManyToManyField(MenuItem)  # Fixed: Many-to-Many relationship

    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)  # Fixed: Removed 'name'

    number_of_order = models.IntegerField()

    PAYMENT_STATUS_CHOICES = [

        ('Successful', 'Successful'),

        ('Pending', 'Pending'),

        ('Cancelled', 'Cancelled')

    ]

    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, default='Pending', max_length=10)

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Confirmed', 'Confirmed'),

        ('In Preparation', 'In Preparation'),

        ('Delivered', 'Delivered'),

        ('Canceled', 'Canceled')

    ]

    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=15)

    take_a_way = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)

    def __str__(self):

        return f"Order {self.id}: {self.payment_status}, {self.status}, Takeaway: {self.take_a_way}"



# #this codes belong to the reza

# class CartItem(models.Model):
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
# #    user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.menu_item.name} X {self.quantity}"   
    
