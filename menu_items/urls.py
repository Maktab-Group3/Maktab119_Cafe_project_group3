from django.urls import path
from . import views

urlpatterns = [
#    path('menu_item/<int:pk>', views.menuitem, name='menu' ), 
    path('menu/', views.menu, name='menu'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('reset-cart/', views.reset_cart, name='reset_cart'),
    path('complete-order/', views.complete_order, name='complete_order'),
]



