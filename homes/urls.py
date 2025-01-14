from django.urls import path
from homes.views import show_home

urlpatterns = [
    path('',show_home,name="home_cafe"),
   
]