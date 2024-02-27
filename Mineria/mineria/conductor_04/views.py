from django.shortcuts import render
from.forms import Conductorform
from django.contrib import messages

# Create your views here.
def conductor(request):
    conductor = Conductorform(request.POST or None)
    if conductor.is_valid():
        conductor.save()
        messages.success(request, 'Conductor guardado con exito')
    return render(request, 'conductor.html', {'conductores': conductor})