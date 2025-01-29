from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

from .models import MenuItem, CartItem



# Menu page

# def menu(request):

#     menu_items = MenuItem.objects.all().order_by('category')

#     return render(request, 'menu_list.html', {'menu_items': menu_items})




# # Add item to session cart

# def add_to_cart(request):

#     if request.method == 'POST':    

#         item_id = request.POST.get('item_id')

#         item = get_object_or_404(MenuItem, id=item_id)



#         # Get the cart from session or initialize it

#         cart = request.session.get('cart', {})



#         # Add the item to the cart (increment quantity if exists)

#         if str(item_id) in cart:

#             cart[str(item_id)]['quantity'] += 1

#         else:

#             cart[str(item_id)] = {'name': item.name, 'price': float(item.price), 'quantity': 1}



#         # Save back to session

#         request.session['cart'] = cart

#         return JsonResponse({'success': True, 'cart': cart})

#     return JsonResponse({'success': False})



# # View cart

# def view_cart(request):

#     cart = request.session.get('cart', {})

#     return render(request, 'cart.html', {'cart': cart})



# # Delete specific item from cart

# def delete_from_cart(request, item_id):

#     cart = request.session.get('cart', {})

#     if str(item_id) in cart:

#         del cart[str(item_id)]

#         request.session['cart'] = cart  # Save back to session

#     return JsonResponse({'success': True, 'cart': cart})



# # Reset the entire cart

# def reset_cart(request):

#     request.session['cart'] = {}

#     return JsonResponse({'success': True, 'cart': {}})



# # Complete order (checkout)

# def complete_order(request):

#     cart = request.session.get('cart', {})

#     if not cart:

#         return JsonResponse({'success': False, 'message': 'Cart is empty!'})



#     # Create a new CartItem

#     cartitem = CartItem.objects.create(total_price=0.0)

#     total_price = 0



#     # Add items to the order

#     for item_id, item_data in cart.items():

#         menu_item = get_object_or_404(MenuItem, id=item_id)

#         cartitem.items.add(menu_item)

#         total_price += menu_item.price * item_data['quantity']



#     # Save total price and clear the cart

#     cartitem.total_price = total_price

#     cartitem.save()

#     request.session['cart'] = {}

#     return JsonResponse({'success': True, 'message': 'Order completed!'})











from django.shortcuts import render

from .models import MenuItem, Category , CartItem

import json



def menu(request):

    # Fetch menu items sorted by category

    categories = Category.objects.prefetch_related('menuitem_set').all()
    sorted_menu = {category.name: category.menuitem_set.all() for category in categories}
    cart = json.loads(request.COOKIES.get('cart', '{}'))
    return render(request, 'menu_list1.html', {'sorted_menu': sorted_menu, 'cart': cart})

def menu_custom(request):
    category_id = request.GET.get('category')
    if category_id:
        menu_items = MenuItem.objects.filter(category_id=category_id)
    else :
        menu_items = MenuItem.objects.all()  

    categories = Category.objects.all()

    return render(request, 'menu_test.html', {'menu_items':menu_items,'categories':categories})      






from django.shortcuts import get_object_or_404, redirect
from .models import MenuItem
import json



def add_to_cart(request):

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(MenuItem, id=item_id)



        # Retrieve the cart from cookies or initialize it

        cart = json.loads(request.COOKIES.get('cart', '{}'))



        # Add item to the cart (or increment quantity if it already exists)

        if item_id in cart:

            cart[item_id]['quantity'] += 1

        else:

            cart[item_id] = {

                'name': item.name,

                'price': float(item.price),

                'quantity': 1,

            }



        # Redirect back to the menu and update the cart cookie

        response = redirect('menu')

        response.set_cookie('cart', json.dumps(cart), max_age=7 * 24 * 60 * 60)  # Save for 7 days

        return response

    return redirect('menu')

def reset_cart(request):

    response = redirect('menu')

    response.delete_cookie('cart')

    return response

def delete_from_cart(request, item_id):
    cart = json.loads(request.COOKIES.get('cart',{}))

    if str(item_id) in cart :
        del cart[str(item_id)]

    response = redirect('menu')
    response.set_cookie('cart',json.dumps(cart), max_age=7 * 24 * 60 * 60)    
    return response

def complete_order(request):

    cart = json.loads(request.COOKIES.get('cart', '{}'))

    if not cart:

        return redirect('menu')  # Redirect if the cart is empty



    # Create a new CartItem instance

    cart_item = CartItem.objects.create(total_price=0.0)

    total_price = 0



    # Add items to the order

    for item_id, item_data in cart.items():

        menu_item = get_object_or_404(MenuItem, id=item_id)

        cart_item.items.add(menu_item)

        total_price += menu_item.price * item_data['quantity']



    # Save the total price and clear the cart

    cart_item.total_price = total_price

    cart_item.save()



    response = redirect('menu')

    response.delete_cookie('cart')  # Clear cart cookie after completing the order

    return response