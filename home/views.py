
from django.shortcuts import render, redirect


def login_principal(request):
    context = {}
    return render(request, 'home/login_principal.html', context)

def home_index(request):
    context = {}
    return render(request, 'home/index.html', context)

def galeria(request):
    context = {}
    return render(request, 'home/galeria.html', context)

def contacto(request):
    context = {}
    return render(request, 'home/contacto.html', context)

def eventos(request):
    context = {}
    return render(request, 'home/eventos.html', context)

def redirigir_login(request):
    tipo_usuario = request.POST.get('tipo_usuario')

    if tipo_usuario == 'artista':
        return  render(request,'artistas/artistas_login.html')
    elif tipo_usuario == 'cliente':
        ## CAMBIAR A LA PAGINA QUE CORRESPONDA
        return  render(request,'clientes/clientes_login.html')
    else:
        
        return render(request, 'home/login-principal.html', {'Indicar tipo de usuario.'})
