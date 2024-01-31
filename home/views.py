
from django.shortcuts import render, redirect
from .views import Artista, Cliente

def login_principal(request):
    context = {}
    return render(request, 'home/login_principal.html', context)

def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def galeria(request):
    context = {}
    return render(request, 'home/galeria.html', context)

def redirigir_login(request):
    tipo_usuario = request.POST.get('tipo_usuario')

    if tipo_usuario == 'artista':
        return  redirect('artista_login')
    elif tipo_usuario == 'cliente':
        ## CAMBIAR A LA PAGINA QUE CORRESPONDA
        return  redirect('cliente_login')
    else:
        
        return render(request, 'home/login_principal.html', {'Indicar tipo de usuario.'})
