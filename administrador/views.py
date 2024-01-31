from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    context={}
    return render (request, 'administrador/index.html', context)


@csrf_protect   
def login_view(request):
    print("en la vista de login")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user != None:
            print("Usuario autenticado:", user)
            auth_login(request, user)
            
            if user.is_staff:
                return redirect("crud_artistas")
            else:
                return redirect("index_home")
        else:
            return render (request, "home/index.html")
    return render (request, "clientes/clientes_login.html")   

def logout_view(request):
    auth_logout(request)
    # Envia al inicio tras cerrar sesion
    return redirect('index_home')  #<---- o la url que coloque aquí    
