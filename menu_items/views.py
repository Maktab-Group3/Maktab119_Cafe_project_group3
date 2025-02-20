from django.shortcuts import render , get_object_or_404
from .models import MenuItem, Category , Comment
from orders.models import Order
import json
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


def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        
        if not item_id or not item_id.isdigit():
            return redirect('/menu/')
        
        item = get_object_or_404(MenuItem, id=item_id)
        discount_stock = int(item.discount_stock)
        cart = json.loads(request.COOKIES.get('cart', '{}'))
        

        if item_id in cart :
            if cart[item_id]['quantity'] < item.entity:
                if discount_stock > 0 :
                    discount_stock -= 1
                    cart[item_id]['quantity'] += 1
                    cart[item_id]['price'] = float(item.discounted_price*cart[item_id]['quantity'])
                else :
                    cart[item_id]['quantity'] += 1
                    cart[item_id]['price']  += float(item.price)
            else:
                return render(request, 'menu_reza.html', {"error": "Not enough stock"})    
        else:
            if discount_stock > 0:
                discount_stock -= 1
                cart[item_id] = {
                    'name': item.name,
                    'price': float(item.discounted_price ),
                    'quantity': 1,
                }
            else :
                cart[item_id] = {
                    'name': item.name,
                    'price': float(item.price ),
                    'quantity': 1,
                }    
        
    
        total_price = sum(item.get('price', 0) for item in cart.values())

        cart['total'] = {'total': total_price}
        
        if request.user.is_authenticated:
            cart['user'] = {'id': request.user.id, 'username': request.user.username}
        
        response = redirect('/menu/')
        response.set_cookie('cart', json.dumps(cart), max_age=5 * 60)
        return response
    
    return redirect('/menu/')

    

def reset_cart(request):

    response = redirect('/menu/')

    response.delete_cookie('cart')

    return response


def delete_from_cart(request, item_id):
    cart = json.loads(request.COOKIES.get('cart', '{}'))

    if item_id in ('total', 'user'):
        return redirect('/menu/')

    if str(item_id) in cart:
        quantity = cart[str(item_id)]['quantity']
        price = cart[str(item_id)]['price'] / quantity 
        

        if quantity > 1:
            cart[str(item_id)]['quantity'] -= 1
            cart[str(item_id)]['price'] = price * cart[str(item_id)]['quantity']
            cart[str(item_id)]['discounted_price'] = discounted_price * cart[str(item_id)]['quantity']
        else:
            del cart[str(item_id)]

    
    total_price = sum(item.get('price', 0) for item in cart.values() if isinstance(item, dict))
    total_discounted_price = sum(item.get('discounted_price', item.get('price', 0)) for item in cart.values() if isinstance(item, dict))

    cart['total'] = {'total': total_price, 'discounted_total': total_discounted_price}

   
    user_data = cart.get('user', None)
    if user_data:
        cart['user'] = user_data

    response = redirect('/menu/')
    response.set_cookie('cart', json.dumps(cart), max_age=5 * 60)
    return response
from django.shortcuts import get_object_or_404, redirect
import json
from .models import MenuItem



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
    discounted_total_price = 0  


    for menu_id, item in cart_items.items():
        if menu_id in ("user", "total"):
            continue
        try:
            menu_item = MenuItem.objects.get(id=int(menu_id)) 
            _quantity = int(item["quantity"])

            if menu_item.entity < _quantity:
                return render(request, "order_detail.html", {"error": f"Not enough stock for: {menu_item.name}"})  

            menu_item.entity -= _quantity
            menu_item.save()

            final_discount = menu_item.discounted_price * _quantity
           
            OrderDetail.objects.create(
                order=order,
                item_name=menu_item.name,
                item_origin_price = menu_item.price,
                item_price=menu_item.discounted_price,  
                discount_price= final_discount,
                quantity = _quantity,
            )


        except (MenuItem.DoesNotExist, ValueError, KeyError):
            continue  

    order.total_price = total_price
    order.discounted_price = final_discount
    order.save()

    response = redirect(reverse("order_detail", args=[order.id]))
    response.delete_cookie("cart")  

    return response



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