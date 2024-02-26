from django.shortcuts import render
from .forms import Transporteform
from  django.contrib import messages
# Create your views here
def transporte(request):
    transporte = Transporteform(request.POST or None)
    if transporte.is_valid():
        transporte.save()
        messages.success(request, 'Transporte guardado con exito')
    return render(request,'transporte.html',{"transportes":transporte})