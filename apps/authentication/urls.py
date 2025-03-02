from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Aqui está o problema
    path('login/', views.my_login, name='my-login'),
    path('register/', views.register, name='register'),  # Aqui está o problema
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='user-logout'),
]