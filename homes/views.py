from django.shortcuts import render
from menu_items.models import MenuItem, Category

def show_home(request):
    category_id = request.GET.get('category')
    if category_id:
        menu_items = MenuItem.objects.filter(category_id=category_id)
    else :
        menu_items = MenuItem.objects.all()  

    categories = Category.objects.all()

    return render(request, 'home_reza_sample.html', {'menu_items':menu_items,'categories':categories})  
def show_menu(request):
    return render(request,'menu.html')

# def show_home(request):
#     data_category=Category.objects.all()
#     contaxe={

#         'cate_show':data_category

#             }
#     return render(request,'home_reza_sample.html',contaxe)

# def create_poll(request):
#     forms=PollCreateForm()
#     contaxe={
#         'form':forms
#     }
#     return render(request,'f.html',contaxe)