
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from gestion.models import Mineral, Transporte, Destino, Envio, Conductor, Inspeccion

class MyAdminSite(admin.AdminSite):
    site_header = 'Mi sitio de administración'
    site_title = 'Mi sitio de administración'
    index_title = 'Inicio'

    def get_app_list(self, request):
        """
        Devuelve una lista ordenada de aplicaciones y modelos para la página de índice.
        """
        app_dict = self._build_app_dict(request)
        # Ordena las aplicaciones alfabéticamente.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Personaliza el orden de tus modelos aquí.
        order = {'User': 1, 'Group': 2, 'Mineral': 3, 'Transporte': 4, 'Destino': 5, 'Envio': 6, 'Conductor': 7, 'Inspeccion': 8}

        # Ordena los modelos dentro de las aplicaciones.
        for app in app_list:
            app['models'].sort(key=lambda x: order.get(x['object_name'], 0))

        return app_list

class MineralAdmin(admin.ModelAdmin):
    list_display =('nombre', 'lugar_extraccion', 'peso','pureza')
    search_fields =('nombre', 'lugar_extraccion', 'peso','pureza')
    list_filter =('nombre',)
    
class TransporteAdmin(admin.ModelAdmin):
    list_display =('matricula', 'tipo_transporte','capacidad_carga', 'fecha_mantenimiento')
    search_fields =('matricula', 'tipo_transporte') 
    list_filter=('matricula',)
    
class DestinoAdmin(admin.ModelAdmin):
    list_display =('estado', 'ciudad', 'direccion')
    search_fields =('estado', 'ciudad', 'direccion')
    list_filter=('estado',)
    
class EnvioAdmin(admin.ModelAdmin):
    list_display =('mineral', 'transporte', 'destino', 'fecha_envio', 'cantidad_mineral')
    search_fields =('mineral', 'transporte', 'destino', 'fecha_envio', 'cantidad_mineral')
    list_filter=('mineral',)
    
class ConductorAdmin(admin.ModelAdmin):
    list_display =('nombre', 'licencia', 'transporte')
    search_fields =('nombre', 'licencia')
    list_filter=('nombre',)
    
class InspeccionAdmin(admin.ModelAdmin):
    list_display =('envio', 'fecha_inspeccion', 'resultado')
    search_fields =('envio', 'fecha_inspeccion', 'resultado')
    list_filter=('envio',)


admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Mineral, MineralAdmin)
admin_site.register(Transporte, TransporteAdmin)
admin_site.register(Destino, DestinoAdmin)
admin_site.register(Envio, EnvioAdmin)
admin_site.register(Conductor, ConductorAdmin)
admin_site.register(Inspeccion, InspeccionAdmin)






