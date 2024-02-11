from django.urls import path
from . import views

urlpatterns = [
    path('', views.mineral_create_view, name='mineral_create_view'),
]
