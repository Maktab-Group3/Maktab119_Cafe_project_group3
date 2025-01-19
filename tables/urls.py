from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_list, name='tables'),
    path('generate_receipt/<int:table_id>/', views.generate_receipt, name='generate_receipt'),
]