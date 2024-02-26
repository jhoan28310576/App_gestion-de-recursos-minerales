from django.shortcuts import render
from .forms import Envioform
from  django.contrib import messages
# Create your views here
def envio(request):
    envio = Envioform(request.POST or None)
    if envio.is_valid():
        envio.save()
        messages.success(request, 'Envio guardado con exito')
    return render(request,'envio.html',{"envios":envio})
