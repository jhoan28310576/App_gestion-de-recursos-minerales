from django.http import JsonResponse
from django.shortcuts import render
from .forms  import Mineralform 
from .models import Mineral
from django.contrib import messages


# Create your views here.

def mineral_list_view (request): 
    mineral = Mineral.objects.all()
    return render(request,'lista_mineral.html', {'mineral': mineral})

'''def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    data = {
        'nombre': mineral.nombre,
        'lugar_extraccion': mineral.lugar_extraccion,
        'peso': str(mineral.peso),
        'pureza': str(mineral.pureza),
    }
    return JsonResponse(data)'''

from django.shortcuts import get_object_or_404


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
def mineral_delete_view(request, id):
    data = dict()
    mineral = get_object_or_404(Mineral, id=id)
    if request.method == 'POST':
        mineral.delete()
        data ['deleted'] = True
        messages.success(request, 'Mineral eliminado con éxito')
    else:
        data['deleted'] = False
    
    return JsonResponse(data)