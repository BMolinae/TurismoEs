from django.shortcuts import render, redirect
from .models import Servicio
from .forms import ServicioForm

def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/listar_servicios.html', {'servicios': servicios})

def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    else:
        form = ServicioForm()

    return render(request, 'servicios/agregar_servicio.html', {'form': form})
