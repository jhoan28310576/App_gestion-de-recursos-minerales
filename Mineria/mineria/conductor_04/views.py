from django.shortcuts import render
from.forms import Conductorform
from django.contrib import messages
from .models import Conductor

# Create your views here.
def conductor(request):
    if request.method == 'POST':
        conductor = Conductorform(request.POST)
        if conductor.is_valid():
            conductor.save()
        messages.success(request, 'Conductor guardado con exito')
        conductor = Conductorform()
    else:
        conductor = Conductorform()
    return render(request, 'conductor.html', {'conductores': conductor})

def conductor_list_view(request):
    conductor = Conductor.objects.all()
    return render(request, 'listar_conductores.html',{'conductor': conductor})