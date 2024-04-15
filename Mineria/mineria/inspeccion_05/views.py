from django.shortcuts import render
from .forms import InspeccionForm
from django.contrib import messages
from .models import Inspeccion
from django.http import JsonResponse


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

def inspeccion_lista_view(request):
    inspeccion_view = Inspeccion.objects.all()
    return render(request, 'listar_inspeccion.html',{'inspeccion_view': inspeccion_view})

'''def load_inspeccion_details(request):
    inspeccion_details_id = request.GET.get('id')
    inspeccion = Inspeccion.objects.get(id=inspeccion_details_id)
    
    data = {'envio': inspeccion.Envio.mineral,
            'fecha_inspeccion': inspeccion.fecha_inspeccion.strftime('%Y-%m-%d %H:%M:%S'),
            'resultado': inspeccion.resultado 
    }
    return JsonResponse(data)'''
        
    
    