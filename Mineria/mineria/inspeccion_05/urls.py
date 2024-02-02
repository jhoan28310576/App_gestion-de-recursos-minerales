from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspeccion, name='inspeccion'),
]