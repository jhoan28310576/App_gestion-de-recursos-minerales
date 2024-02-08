from django.shortcuts import render
from .models import Envio
# Create your views here.
def envio(resquest):
    envio = Envio.objects.all()
    return render(resquest, 'envio.html',{"envios":envio})

