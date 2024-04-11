from django.shortcuts import render
from .forms import Envioform
from .models import Envio
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from  django.contrib import messages
# Create your views here
def envio(request):
    if request.method == 'POST':
        envio = Envioform(request.POST)
        if envio.is_valid():
            envio.save()
        messages.success(request, 'Envio guardado con exito')
        envio  = Envioform(request.POST)
    else:
        envio = Envioform()
    return render(request,'envio.html',{"envios":envio})

def envio_list_view(request):
    envio = Envio.objects.all()
    return render(request, 'listar_envios.html',{'envio': envio})

class MineralSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Model):
            return obj.nombre  # Suponiendo que 'nombre' es un campo serializable de Mineral
        return super().default(obj)
    
def load_envio_details(request):
    envio_id = request.GET.get('id')
    envio = Envio.objects.get(id=envio_id)
    
    data = {
        'mineral': envio.mineral.nombre,  # Suponiendo que 'nombre' es un campo serializable de Mineral
        'transporte': envio.transporte.matricula,
        'destino': envio.destino.estado,
        'fecha_envio': envio.fecha_envio.strftime('%Y-%m-%d %H:%M:%S'),
        'cantidad_mineral': str(envio.cantidad_mineral)
    }
    
    return JsonResponse(data)

class DeleteenvioView(View):
    def delete(self, request, *args, **kwargs):
        envio = Envio.objects.get(pk=self.kwargs['id'])
        envio.delete()
        return JsonResponse({'success': True})

