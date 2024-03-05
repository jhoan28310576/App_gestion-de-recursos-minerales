from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.mineral_list_view, name='mineral_list_view'), 
    path('crear', views.mineral_create_view, name='mineral_create_view'),
    path('eliminar/<int:id>', views.mineral_delete_view, name='mineral_delete_view'),
    path('mineral_detail/<int:id>/', views.mineral_detail, name='mineral_detail'),

]
