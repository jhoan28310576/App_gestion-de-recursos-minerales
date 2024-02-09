from django.shortcuts import render
from .model import gestion


# Create your views here.
def index(request):
    gestions =  gestion.objects.all()
    return render (request, "index.html",{"gestion":gestions})
    
def individual(request):
    try:
        contenido = gestion.objects.get(id=1)  # Cambia 'MiModelo' por el nombre de tu modelo y '1' por el ID del objeto que quieres obtener
    except gestion.DoesNotExist:
        raise Http404("El contenido no existe")
    return render(request, 'index.html', {'individuall': contenido})
    
