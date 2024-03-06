from django.urls import path
from . import views

urlpatterns = [
    path('crear', views.mineral_create_view, name='mineral_create_view'),
    path('listar', views.mineral_list_view, name='mineral_list_view'), 
    path('load_mineral_details/', views.load_mineral_details, name='load_mineral_details'),
    path('delete_mineral/', views.delete_mineral, name='delete_mineral'),
    
    
]
