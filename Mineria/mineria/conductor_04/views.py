from django.shortcuts import render
from.forms import Conductorform
from django.contrib import messages

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