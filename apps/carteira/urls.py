from django.urls import path
from . import views

urlpatterns = [
    path('', views.apps.carteira, name='carteira'),
]