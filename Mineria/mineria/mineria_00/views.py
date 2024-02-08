from django.shortcuts import render
from .models import Mineral
# Create your views here.
def mineria(request):
    mineria = Mineral.objects.all()
    return render (request, "mineria.html",{"mineral":mineria})