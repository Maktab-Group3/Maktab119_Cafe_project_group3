from django.shortcuts import render
from menu_items.models import Category

# Create your views here.

def show_home(request):
    data_category=Category.objects.all()
    contaxe={

        'cate_show':data_category

            }
    return render(request,'base.html',contaxe)

def create_poll(request):
    forms=PollCreateForm()
    contaxe={
        'form':forms
    }
    return render(request,'f.html',contaxe)