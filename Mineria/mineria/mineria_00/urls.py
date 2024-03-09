from django.urls import path
from . import views
from .views import DeleteMineralView

urlpatterns = [
    path('crear/', views.mineral_create_view, name='mineral_create_view'),
    path('listar/', views.mineral_list_view, name='mineral_list_view'), 
    path('load_mineral_details/', views.load_mineral_details, name='load_mineral_details'),
    path('delete_mineral/<int:id>/', DeleteMineralView.as_view(), name='delete_mineral'), 
]
