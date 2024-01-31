from django.shortcuts import render, redirect
from .models import Obra  
from django.contrib.auth.decorators import login_required
from .forms import ObraForm  

# Cambiado el nombre de las vistas y las variables
def crud_obras(request):
    obras = Obra.objects.all()
    context = {'obras': obras}
    print("estoy enviando datos")
    return render(request, "obras/obras_list.html", context)

def obras_add(request):
    context = {}

    if request.method == "POST":
        form = ObraForm(request.POST)
        if form.is_valid():
            print("Dato valido")
            form.save()

            # Limpiar form
            form = ObraForm()

            context = {'mensaje': "Obra guardada correctamente", "form": form}
            return render(request, "obras/obras_add.html", context)
    else:
        form = ObraForm()
        context = {'form': form, 'pedido_choices': Obra.pedido_choices}
        return render(request, 'obras/obras_add.html', context)

def obras_edit(request, pk):
    obra = Obra.objects.get(id_obra=pk)
    if request.method == "POST":
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obras_edit', pk=pk)
    else:
        form = ObraForm(instance=obra)
        context = {'obra': obra, 'form': form}
        return render(request, 'obras/obras_edit.html', context)

def obras_del(request, pk):
    mensajes = []
    errores = []
    obras = Obra.objects.all()
    try:
        obra = Obra.objects.get(id_obra=pk)
        context = {}
        if obra:
            obra.delete()
            mensajes.append("Datos eliminados correctamente")
            context = {'obras': obras, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'obras/obras_list.html', context)
        else:
            context = {}
            return render(request, 'obras/obras_list.html', context)
    except:
        print("Error, Obra no existe")
        obras = Obra.objects.all()
        mensaje = "Error, Obra no existe"
        context = {'mensaje': mensaje, 'obras': obras}
        return render(request, 'obras/obras_list.html', context)


