from django.urls import path
from . import views

urlpatterns = [
    path('', views.destino, name='destino')
]