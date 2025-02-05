from django.urls import path
from . import views

urlpatterns = [
    path('receipt/', views.receipt_view, name='receipt_view'),
    path('/',views.home , name='home')
]
