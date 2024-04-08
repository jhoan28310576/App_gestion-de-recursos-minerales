from django.shortcuts import render
from .forms import Destinoform
from .models import Destino
from django.http import JsonResponse
from django.views import View
from  django.contrib import messages
# Create your views here
def destino(request):
    if request.method == 'POST':
        destino = Destinoform(request.POST)
        if destino.is_valid():
            destino.save()
        messages.success(request, 'Destino guardado con exito')
        destino = Destinoform(request.POST)
    else:
        destino = Destinoform()   
    return render(request,'destino.html',{"destinos":destino})

def destino_list_view(request):
    destino = Destino.objects.all()
    return render(request, 'listar_destinos.html', {'destino': destino})


def load_destino_details(request):
    destino_id = request.GET.get('id')
    destino = Destino.objects.get(id=destino_id)
    data = {'estado': destino.estado, 'ciudad': destino.ciudad, 'direccion': destino.direccion}
    return JsonResponse(data)

class DeletedestinoView(View):
    def  delete(self, request, *args, **kwargs):
        destino = Destino.objects.get(pk=self.kwargs['id'])
        destino.delete()
        return JsonResponse({'success': True})