from django.shortcuts import render
from .models import Destino
# Create your views here.
def destino(resquest):
    destino = Destino.objects.all()
    return render(resquest, 'destino.html',{"destinos":destino})

