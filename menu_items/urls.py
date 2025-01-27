from django.urls import path
from menu_items import views

urlpatterns = [
    path('menu_item/<int:pk>', views.menuitem, name='menuitem' ),
    path('set-cookie/', views.set_cookie_view, name='set_cookie'),
    path('get-cookie/', views.get_cookie_view, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie_view, name='delete_cookie'),
    path('update-cookie/', views.update_cookie_view, name='update_cookie'),    
]



