from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from django.contrib.auth.models import User

#Registrar usuario
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Autenticar usuario
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }

    
