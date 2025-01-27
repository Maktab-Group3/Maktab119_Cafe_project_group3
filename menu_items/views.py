from django.shortcuts import render
from .models import MenuItem, Category
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
def category(request):
    category = MenuItem.objects.all()
    return render(request, 'category.html', {'category':category})
def menuitem(request,pk):
    menuitem = MenuItem.objects.get(id=pk)
    return render(request, 'menuitem.html', {'menuitem':menuitem})




# 1. تنظیم کوکی
def set_cookie_view(request):
    response = HttpResponse("Cookie has been set!")
    # داده‌های نمونه برای کوکی (می‌توانید از request.POST یا request.GET بگیرید)
    data = {"Pizza": 2, "Burger": 1}
    response.set_cookie(
        key='menuItems',  # نام کوکی
        value=json.dumps(data),  # مقدار کوکی (JSON)
        max_age=7 * 24 * 60 * 60,  # زمان انقضا: 7 روز
    )
    return response


# 2. دریافت کوکی
def get_cookie_view(request):
    menu_items = request.COOKIES.get('menuItems')  # خواندن مقدار کوکی
    if menu_items:
        data = json.loads(menu_items)  # تبدیل JSON به دیکشنری
        return JsonResponse({'message': 'Cookie found!', 'data': data})
    else:
        return JsonResponse({'message': 'No cookie found.'})


# 3. حذف کوکی
def delete_cookie_view(request):
    response = HttpResponse("Cookie has been deleted!")
    response.delete_cookie('menuItems')  # حذف کوکی با نام menuItems
    return response


# 4. آپدیت کوکی
def update_cookie_view(request):
    menu_items = request.COOKIES.get('menuItems')  # خواندن کوکی
    if menu_items:
        data = json.loads(menu_items)  # تبدیل JSON به دیکشنری
    else:
        data = {}

    # گرفتن آیتم و تعداد از درخواست (مثلاً از POST یا GET)
    item = request.GET.get('item', None)
    quantity = int(request.GET.get('quantity', 0))

    if item:
        if item in data:
            data[item] += quantity  # تعداد را اضافه می‌کنیم
        else:
            data[item] = quantity  # آیتم جدید اضافه می‌کنیم

    # ذخیره کوکی جدید
    response = JsonResponse({'message': 'Cookie updated!', 'data': data})
    response.set_cookie(
        key='menuItems',
        value=json.dumps(data),
        max_age=7 * 24 * 60 * 60,
    )
    return response
