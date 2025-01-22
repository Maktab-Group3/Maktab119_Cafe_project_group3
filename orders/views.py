from django.shortcuts import render
# from django.http import HttpResponse
from .models import Receipt
from .models import Order
# Create your views here.


def get_all_receipts(request):
    receipts = Receipt.objects.all()
    receipts_dict = {'receipt':receipts}

    
    return render(request,"test.html",receipts_dict)



def get_all_orders(request):
    orders = Order.objects.all()
    
    return render(request,"test.html",{'Order':orders})