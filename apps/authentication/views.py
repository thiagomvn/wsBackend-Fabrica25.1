from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CreateUserForm

def my_login(request):
    form = LoginForm()  # Corrigido: Removido 'www.y'
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Corrigido: Usar 'auth_login' em vez de 'login'
                return redirect('dashboard')

    context = {'loginform': form}
    return render(request, 'authentication/my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect("my-login")

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'authentication/dashboard.html')