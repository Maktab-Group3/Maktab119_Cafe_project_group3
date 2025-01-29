from django.shortcuts import render , get_object_or_404, HttpResponse
from .models import MenuItem, Category
<<<<<<< HEAD
import json
from django.http import JsonResponse


=======
from django.http import JsonResponse, HttpResponse
import json
>>>>>>> 35523a58023033afc464c4cab356be9d8d11e507

# Create your views here.

def show_all_menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'menu_items': menu_items})

def menu(request):
    category_id = request.GET.get('category')
    if category_id:
        menu_items = MenuItem.objects.filter(category_id=category_id)
    else :
        menu_items = MenuItem.objects.all()  

    categories = Category.objects.all()

    return render(request, 'menu_test.html', {'menu_items':menu_items,'categories':categories})      


    

def category(request):
<<<<<<< HEAD
    category = Category.objects.all()
    return render(request, 'menu.html', {'category':category})



=======
    category = MenuItem.objects.all()
    return render(request, 'category.html', {'category':category})
>>>>>>> 35523a58023033afc464c4cab356be9d8d11e507
def menuitem(request,pk):
    menuitem = MenuItem.objects.get(id=pk)
    return render(request, 'menuitem.html', {'menuitem':menuitem})

<<<<<<< HEAD
#these functions are for  shopping cart
def view_cart(request):
    cart = request.COOKIES.get('cart')
    print(cart)
    items = []
    total_price = 0
    for menu_item_id, quantity in cart.items():

        menu_item = get_object_or_404(MenuItem, id=menu_item_id)

        total_price += menu_item.price * quantity

        items.append({

            'menu_item': menu_item,

            'quantity': quantity,

            'subtotal': menu_item.price * quantity,

        })



    return render(request, 'view_cart.html', {'items': items, 'total_price': total_price})

def menu_item_api(request, menu_item_id):

    menu_item = get_object_or_404(MenuItem, id=menu_item_id)

    return JsonResponse({

        'id': menu_item.id,

        'name': menu_item.name,

        'price': float(menu_item.price),

        'description': menu_item.description,

        'image': menu_item.image.url if menu_item.image else None,

    })

def add_to_cart(request):
    cart = request.se


def review_cookie(request):
    name = request.COOKIES.get('icelate') 
    print("*"*10)   
    print(name)
    return HttpResponse("hi")

def cookie_back(request):
    response = HttpResponse("کوکی تنظیم شد!")
    response.set_cookie('username', 'Ali', max_age=3600) # ذخیره برای 1 ساعت
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'کاربر ناشناس')
    return HttpResponse(f'نام کاربر: {username}')


=======



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
>>>>>>> 35523a58023033afc464c4cab356be9d8d11e507
