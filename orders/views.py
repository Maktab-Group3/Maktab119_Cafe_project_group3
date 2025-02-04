from django.shortcuts import render , get_object_or_404
# from django.http import HttpResponse
# from .models import Receipt
from .models import Order
# Create your views here.


def get_all_receipts(request):
    receipts = Receipt.objects.all()
    receipts_dict = {'receipt':receipts}

    
    return render(request,"test.html",receipts_dict)



# def get_all_orders(request,order_id):

#     order = get_object_or_404(Order, id=order_id)
#     print("*"*20)
#     print(order.id)
#     return render(request,"orders.html",{'Order':order})

def get_all_orders(request):
    orders = Order.objects.all()
    return render(request, "all_orders.html",{'Orders':orders})