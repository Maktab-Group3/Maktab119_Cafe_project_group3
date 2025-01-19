from django.urls import path
from menu_items import views

urlpatterns = [
    path('menu_item/<int:pk>', views.menuitem, name='menuitem' )
        
]