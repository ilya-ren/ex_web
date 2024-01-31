from django.urls import path
from . import views
from home.views import home_index
from obras.views import crud_obras
from clientes.views import crud_clientes




urlpatterns = [

    path('crud_artistas', views.crud_artistas, name='crud_artistas'),
    path('artistas_add', views.artistas_add, name='artistas_add'),
    path('artistas_edit/<str:pk>', views.artistas_edit, name='artistas_edit'),
    path('artistas_del/<str:pk>', views.artistas_del, name='artistas_del'),
    path('artistas_login/', views.iniciar_sesion_artista, name='iniciar_sesion_artista'),
    path('home_index/', home_index, name="home_index"),
    path('crud_obras/', crud_obras, name="crud_obras"),
    path('crud_clientes/', crud_clientes, name="crud_clientes"),

  
    
]