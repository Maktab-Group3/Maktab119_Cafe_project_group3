from django.shortcuts import render , get_object_or_404
from .models import MenuItem, Category , Comment
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


# def menu_custom(request):
#     category_id = request.GET.get('category')
#     if category_id:
#         menu_items = MenuItem.objects.filter(category_id=category_id)
#     else :
#         menu_items = MenuItem.objects.all()  

#     categories = Category.objects.all()

#     return render(request, 'home_reza_sample.html', {'menu_items':menu_items,'categories':categories})      






from django.shortcuts import get_object_or_404, redirect
from .models import MenuItem
import json

from django.contrib.auth.models import User

def menu(request):
    categories = Category.objects.prefetch_related('menu_items').all()
    sorted_menu = {category.name: category.menu_items.all() for category in categories}
    cart = json.loads(request.COOKIES.get('cart', '{}')) 
    user_info = cart.get('user',None)
    return render(request, 'menu_reza.html', {'sorted_menu': sorted_menu, 'cart': cart, 'user_info':user_info})
# def add_to_cart(request):

def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        
        # Validate item_id
        if not item_id or not item_id.isdigit():
            return redirect('/menu/')
        
        item = get_object_or_404(MenuItem, id=item_id)
        cart = json.loads(request.COOKIES.get('cart', '{}'))
        
        if item_id in cart:
            if cart[item_id]['quantity'] < item.entity:
                cart[item_id]['quantity'] += 1
                cart[item_id]['price'] = cart[item_id]['quantity'] * item.price
            else :
                return render(request, 'menu_reza.html', {"error": f"not enough stock"})    
        else:
            cart[item_id] = {
                'name': item.name,
                'price': float(item.price),
                'quantity': 1,
            }
        
        # Recalculate total
        total_price = sum(item.get('price', 0) for item in cart.values())
        cart['total'] = {'total': total_price}
        
        # Add user data if authenticated
        if request.user.is_authenticated:
            user_data = {'id': request.user.id, 'username': request.user.username}
            cart['user'] = user_data
        
        response = redirect('/menu/')
        response.set_cookie('cart', json.dumps(cart), max_age=5 * 60)
        return response
    
    return redirect('/menu/')

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


        total_price = sum(int(item['price']) * item['quantity'] for item in cart.values())
        cart['total'] = {'total': total_price}
        if request.user.is_authenticated:
            user_data = {'id': request.user.id, 'username': request.user.username}
            cart['user'] = user_data
        # Redirect back to the menu and update the cart cookie
        response = redirect('/menu/')
        response.set_cookie('cart', json.dumps(cart), max_age= 5 * 60)  
        return response

    return redirect('/menu/')

def reset_cart(request):

    response = redirect('/menu/')

    response.delete_cookie('cart')

    return response

# def delete_from_cart(request, item_id):
    cart = json.loads(request.COOKIES.get('cart',{}))
    user_data = cart.get('user', None)
    quantity = cart[str(item_id)]['quantity']
    total_price = cart[str(item_id)]['price']
    price = cart[str(item_id)]['price']/cart[str(item_id)]['quantity']
    if str(item_id) in cart :
        if cart[str(item_id)]['quantity'] > 1 :
            cart[str(item_id)]['quantity'] -= 1
            cart[str(item_id)]['price'] = price*cart[str(item_id)]['quantity']
            
        else :
            del  cart[str(item_id)]   
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    cart['total'] = {'total': total_price}
    if user_data:
        cart['user'] = user_data
    response = redirect('/menu/')
    response.set_cookie('cart',json.dumps(cart), max_age= 5 * 60)    
    return response
    # cart = json.loads(request.COOKIES.get('cart', {}))
    # if str(item_id) in cart:
    #     price_per_item = cart[str(item_id)]['price'] / cart[str(item_id)]['quantity']
        
    #     # کاهش تعداد یا حذف آیتم از سبد خرید
    #     if cart[str(item_id)]['quantity'] > 1:
    #         cart[str(item_id)]['quantity'] -= 1
    #         cart[str(item_id)]['price'] = price_per_item * cart[str(item_id)]['quantity']
    #     else:
    #         del cart[str(item_id)]  # حذف آیتم از سبد خرید
        
    #     # محاسبه قیمت کل سبد خرید
    #     total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    #     cart['total'] = {'total': total_price}  # بروزرسانی قیمت کل
        
    #     response = redirect('/menu/')
    #     response.set_cookie('cart', json.dumps(cart), max_age=5 * 60)
    #     response.set_cookie('cart_total', total_price, max_age=5 * 60)  # بروزرسانی قیمت کل در کوکی
    #     return response

def delete_from_cart(request, item_id):
    cart = json.loads(request.COOKIES.get('cart', '{}'))
    
    # Ensure item_id is not 'total' or 'user'
    if item_id in ('total', 'user'):
        return redirect('/menu/')
    
    if str(item_id) in cart:
        quantity = cart[str(item_id)]['quantity']
        price = cart[str(item_id)]['price'] / quantity
        
        if quantity > 1:
            cart[str(item_id)]['quantity'] -= 1
            cart[str(item_id)]['price'] = price * cart[str(item_id)]['quantity']
        else:
            del cart[str(item_id)]
    
    # Recalculate total
    total_price = sum(item.get('price', 0) for item in cart.values())

    cart['total'] = {'total': total_price}
    
    # Preserve user data if it exists
    user_data = cart.get('user', None)
    if user_data:
        cart['user'] = user_data
    
    response = redirect('/menu/')
    response.set_cookie('cart', json.dumps(cart), max_age=5 * 60)
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

 
    order = Order.objects.create(user=request.user, table=default_table)

    total_price = 0
    for menu_id, item in cart_items.items():
        if menu_id == "user" or menu_id == "total":
            continue
        try:
            menu_item = MenuItem.objects.get(id=int(menu_id)) 
            quantity = int(item["quantity"])

            if menu_item.entity < quantity :
                return render(request, "order.html", {"error": f"not enough stock or entity of : {menu_item.name}"})  
            
            menu_item.entity -= quantity
            menu_item.save()
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

@login_required(login_url='/login/')  
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderDetail.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order':order,'order_items':order_items})





from .forms import CommentForm

def menu_item_detail(request, item_id):

    menu_item = get_object_or_404(MenuItem, id=item_id)

    comments = menu_item.comments.all()  

    form = CommentForm()



    if request.method == 'POST':

        if request.user.is_authenticated:

            form = CommentForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)

                comment.menu_item = menu_item

                comment.user = request.user

                comment.save()

                return redirect('menu_item_detail', item_id=menu_item.id)

        else:

            return redirect('login')  



    return render(request, 'menu_item_detail.html', {'menu_item': menu_item, 'comments': comments, 'form': form})