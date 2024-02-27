from django.shortcuts import render
from .forms import InspeccionForm
from django.contrib import messages

# Create your views here.
def inspeccion(request):
    inspeccion = InspeccionForm (request.POST or None)
    if inspeccion.is_valid():
        inspeccion.save()
        messages.success(request, 'Inspeccion guardado con exito')
    return render(request,'inspeccion.html',{'inspecciones':inspeccion})