from django.shortcuts import render
from .models import MenuItem, Category

# Create your views here.
def category(request):
    category = MenuItem.objects.filter('category' = category)
    return render(request, 'category.html', {'category':category})
def menuitem(request,pk):
    menuitem = MenuItem.objects.get(id=pk)
    return render(request, 'menuitem.html', {'menuitem':menuitem})
