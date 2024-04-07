from django.shortcuts import render
from .forms import Destinoform
from .models import Destino
from  django.contrib import messages
# Create your views here
def destino(request):
    if request.method == 'POST':
        destino = Destinoform(request.POST)
        if destino.is_valid():
            destino.save()
        messages.success(request, 'Destino guardado con exito')
        destino = Destinoform(request.POST)
    else:
        destino = Destinoform()   
    return render(request,'destino.html',{"destinos":destino})

def destino_list_view(request):
    destino = Destino.objects.all()
    return render(request, 'listar_destinos.html', {'destinos': destino})


