from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import aauthenticate , login, logout

# Create your views here.
    
################## login #####################

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_obj = AuthenticationForm()
    if request.method == 'POST':
        form_obj = AuthenticationForm(data=request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data['username']
            password = form_obj.cleaned_data['password']
            user = aauthenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                return redirect(next_page)
            else:
            
                return HttpResponse('invalid login')
        else:
            print(form_obj.errors)    
    context = {
        'form': form_obj
    }
    return render(request, ".......html", context)

################## logout #####################

def logout_view(request):
    # if request.user.is_authenticated():
    logout(request)
    # return HttpResponse('you are logged out')
    return redirect('/')

################## signup #####################

def signup_view(request):
    form_obj = UserCreationForm()
    if request.method == 'POST' :
        form_obj = UserCreationForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/login')

        else:
            pass
    context = {
        'form' : form_obj
    }

    return render(request, '.............html', context)

