from django.shortcuts import render
from .forms  import Mineralform 
from django.contrib import messages

# Create your views here.
def mineral_create_view (request):
    form = Mineralform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mineral guardado con exito')
    return render(request, 'mineria.html', {'form': form})
   