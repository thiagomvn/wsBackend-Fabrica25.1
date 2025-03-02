from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth  #Funções de autenticação do Django	
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'authentication/index.html')

def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
        
    context = {'registerform':form}

    return render(request, 'authentication/register.html', context=context)
        

def my_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    
    context = {'loginform':form}

    return render(request, 'authentication/my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect("my-login")

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'authentication/dashboard.html')
