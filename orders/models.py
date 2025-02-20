from django.db import models

from tables.models import Table
# from tables.models import Table



class TimeStampeMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

from django.contrib.auth.models import User

class Order(TimeStampeMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, name='table')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    payment_status = models.CharField(
        choices=[('Successful', 'Successful'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')],
        default='Pending', max_length=10
    )
    status = models.CharField(
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('In Preparation', 'In Preparation'),
            ('Delivered', 'Delivered'),
            ('Canceled', 'Canceled')
        ],
        default='Pending', max_length=20
    )
    take_a_way = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)  # اضافه شده برای تاریخ ایجاد
    # updated_at = models.DateTimeField(auto_now=True)  # اضافه شده برای تاریخ به روز رسانی

    def __str__(self):
        return f"Order {self.id} - Status: {self.status}, Payment: {self.payment_status}, Takeaway: {self.take_a_way}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    item_name = models.CharField(max_length=255)  
    item_origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField()
    def total_item_price(self):

        return self.item_price * self.quantity  

    def __str__(self):

        return f"{self.item_name} x{self.quantity} - {self.order}"

    
class Receipt(TimeStampeMixin):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reciept for order {self.order.id} "
    
    def __str__(self):
        return f'{self.id}'
   