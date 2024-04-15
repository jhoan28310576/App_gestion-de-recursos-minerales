from django.shortcuts import render
from.forms import Conductorform
from django.contrib import messages
from .models import Conductor
from django.http import JsonResponse
from django.views import View 

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

def load_conductor_details(request):
    conductor_id = request.GET.get('id')
    conductor  = Conductor.objects.get(id=conductor_id)
    data  = {'nombre': conductor.nombre, 'licencia': conductor.licencia, 'transporte': conductor.transporte.matricula }
    return JsonResponse(data)

class DeleteconductorView(View):
    def delete(self, request, *args, **kwargs):
        conductorDelete = Conductor.objects.get(pk=self.kwargs['id'])
        conductorDelete.delete()
        return JsonResponse({'success': True})