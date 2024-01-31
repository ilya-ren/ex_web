from django.urls import path
from . import views



urlpatterns = [
    path('crud_obras', views.crud_obras, name='crud_obras'),
    path('obras_add', views.obras_add, name='obras_add'),
    path('obras_edit/<str:pk>', views.obras_edit, name='obras_edit'),
    path('obras_del/<str:pk>', views.obras_del, name='obras_del')
]