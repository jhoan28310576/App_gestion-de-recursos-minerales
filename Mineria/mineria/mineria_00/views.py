from django.shortcuts import render
from .forms  import Mineralform 
from django.contrib import messages

# Create your views here.
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
   