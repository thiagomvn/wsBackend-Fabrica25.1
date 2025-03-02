from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_carteiras, name='lista_carteiras'),
    path('<int:pk>/', views.detalhe_carteira, name='detalhe_carteira'),
    path('criar/', views.criar_carteira, name='criar_carteira'),
    path('<int:pk>/atualizar/', views.atualizar_carteira, name='atualizar_carteira'),
    path('<int:pk>/deletar/', views.deletar_carteira, name='deletar_carteira'),
    path('taxa-cambio/', views.taxa_cambio, name='taxa_cambio'),
]