from django.urls import path
from . import views

urlpatterns = [
    path('', views.envio, name='envio'),
]
