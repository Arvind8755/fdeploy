from django.shortcuts import render
from django.template import context, loader
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth

# Create your views here.
@login_required(login_url='login')
def home(request):
  return render(request, "app1/home.html")

def SignupPage(request):
  
    return render(request, 'app1/signup.html')

def LoginPage(request):
 
    return render (request,'app1/login.html')


 


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'registerform': form}
    return render(request, 'app1/register.html', context=context)


def LoginPage(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")  # Change 'home' to your actual home route

    else:  # Handles GET requests
        form = LoginForm()  # Ensure form is defined for GET requests

    return render(request, "app1/login.html", {"form": form})

def LogoutPage(request):
    logout(request)
    return redirect('login')








