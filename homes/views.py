from django.shortcuts import render

# Create your views here.
def show_home(request):
    return render(request,'base.html')
def show_menu(request):
    return render(request,'menu.html')

def show_order(request):
    return render(request,'order.html')


# from django.shortcuts import render, redirect
# from .forms import PollForm


# def home_poll(request):
#     if request.method == 'POST':
#         form = PollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home') #replace it after termin with fardin
#     else:
#         form = PollForm()
#     return render(request, '',{'form'.form})     