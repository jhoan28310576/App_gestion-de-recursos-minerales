from django.shortcuts import render
from .forms import Transporteform
from .models import Transporte
from django.http import JsonResponse
from  django.contrib import messages
from django.views import View
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

def transport_list_view (request): 
    transport = Transporte.objects.all()
    return render(request,'lista_transporte.html', {'transporte': transport})


def load_transport_details(request):
    transport_id = request.GET.get('id')
    transport = Transporte.objects.get(id=transport_id)
    data = {'matricula': transport.matricula, 'tipo_transporte': transport.tipo_transporte, 'capacidad_carga': transport.capacidad_carga, 'fecha_mantenimiento': transport.fecha_mantenimiento}
    return JsonResponse(data)


class DeletetransportView(View):
    def delete(self, request, *args, **kwargs):
        transport = Transporte.objects.get(pk=self.kwargs['id'])
        transport.delete()
        return JsonResponse({'success': True})

