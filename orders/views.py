from django.shortcuts import render , get_object_or_404
# from django.http import HttpResponse
# from .models import Receipt
from .models import Order, OrderDetail
# Create your views here.
from .models import Receipt
from datetime import datetime
import random
from decimal import Decimal

def get_all_receipts(request):
    receipts = Receipt.objects.all()
    receipts_dict = {'receipt':receipts}

    
    return render(request,"test.html",receipts_dict)


from django.contrib.auth.decorators import login_required

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('details')
    # order_items = OrderDetail.objects.all()
    return render(request, 'orders.html', {'orders':orders})



def receipt_view(request):
    receipt_id = request.GET.get('receipt_id')  # دریافت شناسه رسید از URL
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # تاریخ و زمان فعلی
    context = {'current_date': current_date}  # مقدار اولیه کانتکست

    if receipt_id and receipt_id.isdigit():  # بررسی مقدار عددی بودن
        receipt = Receipt.objects.filter(id=int(receipt_id)).first()  # دریافت رسید

        if receipt:
            # اگر is_refunded=True باشد، تخفیف بین ۵ تا ۳۰ درصد اعمال شود
            discount_percentage = random.randint(5, 30) if receipt.is_refunded else 0

            # محاسبه قیمت بعد از تخفیف
            discounted_price = round(Decimal(receipt.total_price) * (1 - Decimal(discount_percentage) / 100), 2)

            # دریافت مقدار order از رسید
            orders = receipt.order

            # افزودن مقادیر به کانتکست
            context.update({
                'receipt': receipt,
                'order': orders,
                'discounted_price': discounted_price,
                'discount_percentage': discount_percentage
            })
        else:
            context['error_message'] = "No receipt found with this ID."  # نمایش پیام خطا

    return render(request, 'test.html', context)
