from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .forms  import Mineralform 
from .models import Mineral
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.

def mineral_list_view (request): 
    mineral = Mineral.objects.all()
    return render(request,'lista_mineral.html', {'mineral': mineral})

def load_mineral_details(request):
    mineral_id = request.GET.get('id')
    mineral = Mineral.objects.get(id=mineral_id)
    data = {'nombre': mineral.nombre, 'lugar_extraccion': mineral.lugar_extraccion, 'peso': mineral.peso, 'pureza': mineral.pureza}
    return JsonResponse(data)

def mineral_detail(request, id):
    mineral = get_object_or_404(Mineral, id=id)
    return render(request, 'mineral_detail.html', {'mineral': mineral})

def mineral_create_view (request):
    if request.method == 'POST':
        form = Mineralform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mineral guardado con exito')
            form = Mineralform()
    else:
        form = Mineralform()
    return render(request, 'mineria.html', {'form': form})

#eliminar, funcion solucionar luego
class DeleteMineralView(View):
    def delete(self, request, *args, **kwargs):
        mineral = Mineral.objects.get(pk=self.kwargs['id'])
        mineral.delete()
        return JsonResponse({'success': True})