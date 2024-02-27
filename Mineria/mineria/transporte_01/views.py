from django.shortcuts import render
from .forms import Transporteform
from  django.contrib import messages
# Create your views here
def transporte(request):
    if request.method == 'POST':
        transporte = Transporteform(request.POST)
        if transporte.is_valid():
            transporte.save()
        messages.success(request, 'Transporte guardado con exito')
        transporte = Transporteform()
    else:
        transporte = Transporteform(request.POST)
    return render(request,'transporte.html',{"transportes":transporte})