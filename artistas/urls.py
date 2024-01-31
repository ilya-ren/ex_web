from django.urls import path
from . import views


urlpatterns = [

    path('crud_artistas', views.crud_artistas, name='crud_artistas'),
    path('artistas_add', views.artistas_add, name='artistas_add'),
    path('artistas_edit/<str:pk>', views.artistas_edit, name='artistas_edit'),
    path('artistas_del/<str:pk>', views.artistas_del, name='artistas_del'),
    path('artistas_login/', views.iniciar_sesion_artista, name='iniciar_sesion_artista'),
  
    
]