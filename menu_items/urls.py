from django.urls import path
from . import views

urlpatterns = [
    path('menu_item/<int:pk>', views.menuitem, name='menuitem' ),
    path('set-cookie/', views.set_cookie_view, name='set_cookie'),
    path('get-cookie/', views.get_cookie_view, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie_view, name='delete_cookie'),
    path('update-cookie/', views.update_cookie_view, name='update_cookie'),    
    path('', views.menu, name='menu'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('reset-cart/', views.reset_cart, name='reset_cart'),
    path('complete-order/', views.complete_order, name='complete_order'),
]



