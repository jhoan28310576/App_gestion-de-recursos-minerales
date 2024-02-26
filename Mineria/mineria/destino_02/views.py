from django.shortcuts import render
from .forms import Destinoform
from  django.contrib import messages
# Create your views here
def destino(request):
    destino = Destinoform(request.POST or None)
    if destino.is_valid():
        destino.save()
        messages.success(request, 'Destino guardado con exito')
    return render(request,'destino.html',{"destinos":destino})
