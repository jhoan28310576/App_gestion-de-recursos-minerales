from django.urls import include, path
from gestion.admin import admin_site
from django.conf import  settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin_site.urls),
    path('gestion/', include('gestion.urls')),  
    path('mineral_create_view/', include('mineria_00.urls')), 
    path('transporte/', include('transporte_01.urls'), name='transporte'), 
    path('destino/', include('destino_02.urls')), 
    path('envio/', include('envio_03.urls')), 
    path('conductor/', include('conductor_04.urls')), 
    path('inspeccion/', include('inspeccion_05.urls')),
    path('img/', include('inspeccion_05.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
