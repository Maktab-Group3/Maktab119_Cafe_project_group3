from django.urls import path
from .views import  orders

urlpatterns = [
    # path('orders/', get_all_orders, name='order_list'),
    path('orders/', orders , name='orders'),
]