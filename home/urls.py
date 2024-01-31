
from django.urls import path
from . import views
from clientes.views import iniciar_sesion_cliente

urlpatterns = [
    path('login-principal/', views.login_principal, name='login-principal'),
    path('redirigir-login/', views.redirigir_login, name='redirigir-login'),
    path('home_index/', views.home_index, name='home_index'),
    path('galeria/', views.galeria, name='galeria'),
    path('clientes/', iniciar_sesion_cliente, name='iniciar_sesion_cliente' ),
    path('contacto/', views.contacto, name='contacto'),
    path('eventos/', views.eventos, name='eventos'),


   
]
