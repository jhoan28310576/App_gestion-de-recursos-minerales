from django.shortcuts import render
from .forms import InspeccionForm
from django.contrib import messages

# Create your views here.
def inspeccion(request):
    if request.method == 'POST':
        inspeccion = InspeccionForm (request.POST)
        if inspeccion.is_valid():
            inspeccion.save()
        messages.success(request, 'Inspeccion guardado con exito')
        inspeccion = InspeccionForm()
    else:
        inspeccion = InspeccionForm()
    return render(request,'inspeccion.html',{'inspecciones':inspeccion})