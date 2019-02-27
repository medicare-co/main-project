from django.shortcuts import render, redirect
from home.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def logout(request):
    args = {'user': request.user}
    return render(request, 'home/logout.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'home/register.html', args)

def about(request):
    return render(request, 'home/about.html')
