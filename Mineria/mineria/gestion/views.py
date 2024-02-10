from django.shortcuts import render
from .model import gestion


# Create your views here.
def index(request):
    try:
        gestions = gestion.objects.filter(id__in=[1, 2, 3])
    except gestion.DoesNotExist:
        raise Http404("El contenido no existe")
    return render(request, 'index.html', {'gestion': gestions})




    
