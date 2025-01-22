from django.shortcuts import render , redirect
from .models import MenuItem, Category , CartItem

# Create your views here.

def show_all_menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})



def category(request):
    category = Category.objects.all()
    return render(request, 'menu.html', {'category':category})



def menuitem(request,pk):
    menuitem = MenuItem.objects.get(id=pk)
    return render(request, 'menuitem.html', {'menuitem':menuitem})

#these functions are for  shopping cart
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    cart_info = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'menu.html', cart_info )



def add_to_cart(request, product_id):
    product = MenuItem.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
        