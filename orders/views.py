from django.shortcuts import render , get_object_or_404
# from django.http import HttpResponse
# from .models import Receipt
from .models import Order, OrderDetail
# Create your views here.


def get_all_receipts(request):
    receipts = Receipt.objects.all()
    receipts_dict = {'receipt':receipts}

    
    return render(request,"test.html",receipts_dict)




def orders(request):
    orders = Order.objects.all()
    # order_items = OrderDetail.objects.all()
    return render(request, 'orders.html', {'orders':orders})