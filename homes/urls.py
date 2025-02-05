from django.urls import path
from homes.views import show_home
urlpatterns = [
    path('',show_home,name="home"),
#    path('menu/',show_menu,name="show menu"),
#    path('order/',show_order,name="show_order")
   
]