from django.urls import path
from . import views

urlpatterns = [
#    path('menu_item/<int:pk>', views.menuitem, name='menuitem' )
    path('menu/', show_all_menu, name = 'all menu')
        
]