from django.urls import path
from .views import get_all_orders

urlpatterns = [
    path('orders/', get_all_orders, name='order_list'),
]