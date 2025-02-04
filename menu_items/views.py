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

    if str(item_id) in cart :
        del cart[str(item_id)]

    response = redirect('/menu/')
    response.set_cookie('cart',json.dumps(cart), max_age= 5 * 60)    
    return response

from django.shortcuts import get_object_or_404, redirect
import json
from .models import MenuItem

def complete_order(request):
    cart = json.loads(request.COOKIES.get('cart', '{}'))

    # Create the order
    order_item = Order(
            number_of_order=1,  # Provide a default value for the required field
            payment_status='Pending',  # Set default payment status
            status='Pending',  # Set default order status
            total_price=0.0  # Initialize total price
    )
    order_item.save()  # Save the order to the database first

    total_price = 0

    # Add items to the order
    for item_id, item_data in cart.items():
        menu_item = get_object_or_404(MenuItem, id=item_id)
        order_item.menu_items.add(menu_item)  # Add the menu item to the order
        total_price += menu_item.price * item_data['quantity']

    # Save the total price and update the order
    order_item.total_price = total_price
    order_item.save()  # Save the order again with the updated total price

    # Clear the cart cookie after completing the order
    response = redirect('order_list')
    response.delete_cookie('cart')

    return response 



