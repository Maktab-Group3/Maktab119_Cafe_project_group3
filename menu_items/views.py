from django.shortcuts import render , get_object_or_404
from .models import MenuItem, Category 
from orders.models import CartItem
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

def complete_order(request):

    cart = json.loads(request.COOKIES.get('cart', '{}'))
    #line 115 make a cart item to save the cookies data to it but it is now empty
    cart_item = CartItem.objects.create(total_price=0.0)
    total_price = 0



    # Add items to the cart item

    for item_id, item_data in cart.items():

        menu_item = get_object_or_404(MenuItem, id=item_id)

        cart_item.items.add(menu_item)

        total_price += menu_item.price * item_data['quantity']



    # Save the total price and clear the cart

    cart_item.total_price = total_price

    cart_item.save()



    response = redirect('/menu/')

    response.delete_cookie('cart')  # Clear cart cookie after completing the order

    return response