from django.shortcuts import render

# Create your views here.
def conductor(request):
    return render(request, 'conductor.html')