from django.urls import path
from . import views

urlpatterns = [
    path('crud_clientes', views.crud_clientes, name='crud_clientes'),
    path('clientes_add', views.clientes_add, name='clientes_add'),
    path('clientes_edit/<str:pk>', views.clientes_edit, name='clientes_edit'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_login/', views.iniciar_sesion_cliente, name='iniciar_sesion_cliente'),
]