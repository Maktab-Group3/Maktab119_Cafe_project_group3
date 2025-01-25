from django.urls import path
from . import views

urlpatterns = [
#    path('menu_item/<int:pk>', views.menuitem, name='menuitem' )
     path('menu/', views.menu, name = 'menu'),
#    path('cart/', views.view_cart, name='view_cart'),
#    path('api/menu_item/<int:menu_item_id>/', views.menu_item_api, name='menu_item_api'),
#    path('cookie/',views.cookie_back)
        
]