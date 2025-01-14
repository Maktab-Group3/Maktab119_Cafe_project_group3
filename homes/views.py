from django.shortcuts import render

# Create your views here.
def show_home(request):
    return render(request,'base.html')





from django.shortcuts import render, redirect
from .forms import PollForm

# Create your views here.
def home_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #replace it after termin with fardin
    else:
        form = PollForm()
    return render(request, '',{'form'.form})     