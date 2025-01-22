from django.shortcuts import render, redirect
from .forms import PollForm


# Create your views here.
def show_home(request):
    return render(request,'base.html')


def home_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html') #replace it after termin with fardin
    else:
        form = PollForm()
    return render(request, '',{'form'.form})     