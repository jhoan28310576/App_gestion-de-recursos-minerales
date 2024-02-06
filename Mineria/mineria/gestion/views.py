from django.shortcuts import render
from .model import gestion


# Create your views here.
def index(request):
    gestions =  gestion.objects.all()
    return render (request, "index.html",{"gestion":gestions})
    
    
