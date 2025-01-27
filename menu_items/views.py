from django.shortcuts import render , get_object_or_404, HttpResponse
from .models import MenuItem, Category
import json
from django.http import JsonResponse



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
    category = Category.objects.all()
    return render(request, 'menu.html', {'category':category})



def menuitem(request,pk):
    menuitem = MenuItem.objects.get(id=pk)
    return render(request, 'menuitem.html', {'menuitem':menuitem})

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


