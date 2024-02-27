from django.shortcuts import render
from .forms import Destinoform
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
