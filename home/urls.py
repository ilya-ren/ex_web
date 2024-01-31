
from django.urls import path
from . import views

urlpatterns = [
    path('login-principal/', views.login_principal, name='login-principal'),
    path('redirigir-login/', views.redirigir_login, name='redirigir-login'),
    path('index/', views.index, name='home-index'),
   
]
