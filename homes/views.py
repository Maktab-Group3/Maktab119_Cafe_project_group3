from django.shortcuts import render

def show_home(request):
    return render(request,'home_reza_sample.html')
def show_menu(request):
    return render(request,'menu.html')

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