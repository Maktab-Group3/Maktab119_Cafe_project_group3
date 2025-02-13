from django.shortcuts import render , get_object_or_404
from .models import MenuItem, Category 
from orders.models import Order
import json


# Create your views here.

# def show_all_menu(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, 'menu_reza.html', {'menu_items': menu_items})

# def menu(request):
#     category_id = request.GET.get('category')
#     if category_id:
#         menu_items = MenuItem.objects.filter(category_id=category_id)
#     else :
#         menu_items = MenuItem.objects.all()  

#     categories = Category.objects.all()

#     return render(request, 'menu_reza.html', {'menu_items':menu_items,'categories':categories})      

# def menuitem(request,pk):
#     menuitem = MenuItem.objects.get(id=pk)
#     return render(request, 'menuitem.html', {'menuitem':menuitem})



def menu(request):
    categories = Category.objects.prefetch_related('menu_items').all()
    sorted_menu = {category.name: category.menu_items.all() for category in categories}
    cart = json.loads(request.COOKIES.get('cart', '{}'))
    return render(request, 'menu_reza.html', {'sorted_menu': sorted_menu, 'cart': cart})

# def menu_custom(request):
#     category_id = request.GET.get('category')
#     if category_id:
#         menu_items = MenuItem.objects.filter(category_id=category_id)
#     else :
#         menu_items = MenuItem.objects.all()  

#     categories = Category.objects.all()

#     return render(request, 'menu_test.html', {'menu_items':menu_items,'categories':categories})      






from django.shortcuts import get_object_or_404, redirect
from .models import MenuItem
import json



def add_to_cart(request):

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(MenuItem, id=item_id)
        cart = json.loads(request.COOKIES.get('cart', '{}'))
        if item_id in cart:

            cart[item_id]['quantity'] += 1
            cart[item_id]['price'] = cart[item_id]['quantity'] * item.price

        else:

            cart[item_id] = {

                'name': item.name,

                'price': float(item.price),

                'quantity': 1,

            }



        # Redirect back to the menu and update the cart cookie

        response = redirect('/menu/')

        response.set_cookie('cart', json.dumps(cart), max_age= 5 * 60)  

        return response

    return redirect('/menu/')

def reset_cart(request):

    response = redirect('/menu/')

    response.delete_cookie('cart')

    return response

def delete_from_cart(request, item_id):
    cart = json.loads(request.COOKIES.get('cart',{}))
    quantity = cart[str(item_id)]['quantity']
    total_price = cart[str(item_id)]['price']
    price = cart[str(item_id)]['price']/cart[str(item_id)]['quantity']
    if str(item_id) in cart :
        if cart[str(item_id)]['quantity'] > 1 :
            cart[str(item_id)]['quantity'] -= 1
            cart[str(item_id)]['price'] = price*cart[str(item_id)]['quantity']
            
        else :
            del  cart[str(item_id)]   

    response = redirect('/menu/')
    response.set_cookie('cart',json.dumps(cart), max_age= 5 * 60)    
    return response

from django.shortcuts import get_object_or_404, redirect
import json
from .models import MenuItem

# def complete_order(request):
#     cart = json.loads(request.COOKIES.get('cart', '{}'))

#     # Create the order
#     order = Order.objects.create()

#     total_price = 0

#     # Add items to the order
#     for item_id, item_data in cart.items():
#         menu_item = get_object_or_404(MenuItem, id=item_id)
#         quantity = item_data['quntity']

#         total_price += menu_item.price * item_data['quantity']

#     # Save the total price and update the order
#     order_item.total_price = total_price
#     order_item.save()  # Save the order again with the updated total price

#     # Clear the cart cookie after completing the order
#     response = redirect('order_list')
#     response.delete_cookie('cart')

#     return response 


import json
from django.shortcuts import render, redirect
from .models import MenuItem
from orders.models import Order, OrderDetail
from tables.models import Table
from django.urls import reverse

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')  
def complete_order(request):
    cart_data = request.COOKIES.get("cart")  

    if not cart_data:
        return render(request, "order.html", {"error": "Your cart is empty!"})

    try:
        cart_items = json.loads(cart_data)  
    except json.JSONDecodeError:
        return render(request, "order.html", {"error": "Invalid cart format!"})

    if not cart_items:
        return render(request, "order.html", {"error": "No items selected!"})

    
    default_table = Table.objects.first()

 
    order = Order.objects.create(table=default_table)

    total_price = 0
    for menu_id, item in cart_items.items():
        try:
            menu_item = MenuItem.objects.get(id=int(menu_id)) 
            quantity = int(item["quantity"])  
            
            OrderDetail.objects.create(
                order=order,
                item_name=menu_item.name,  
                item_price=menu_item.price,  
                quantity=quantity
            )

            total_price += menu_item.price * quantity  
        except (MenuItem.DoesNotExist, ValueError, KeyError):
            continue  
       
    order.total_price = total_price
    order.save() 

    response = redirect(reverse("order_detail", args=[order.id]))  
    response.delete_cookie("cart")  

    return response
# def order_detail(request, order_id):
#     order_id = int(order_id)
#     order = get_object_or_404(Order, "orders.html", id = order_id)
#     order_items = OrderDetail.objects.filter(order=order)
#     return render(request, "orders.html", {'order':order, 'order_item':order_items})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderDetail.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order':order,'order_items':order_items})