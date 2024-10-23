from django.shortcuts import render,get_object_or_404,redirect
from .forms import RegisterUserForm,LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home')
        else:
            form = RegisterUserForm()
        context = {'form':form}
        return render(request,'accounts/register.html',context)
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                return redirect('home')
            messages.error(request,"No user with provided details")
        messages.error(request,"Errors with form input")
    form = LoginForm()
    context = {"form":form}
    return render(request,'accounts/login.html',context)
def homepage(request):
    context = {}
    return render(request,'homepage.html',context)
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home')
        else:
            form = RegisterUserForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)