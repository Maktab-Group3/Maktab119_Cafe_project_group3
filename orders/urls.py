from django.urls import path
from .views import  orders, receipt_view

urlpatterns = [
    # path('orders/', get_all_orders, name='order_list'),
    path('orders/', orders , name='orders'),
    path('receipt/', receipt_view, name='receipt_view'),
]