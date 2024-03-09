import os
from django.core.management.base import BaseCommand
from mineria_00.models import Mineral

os.environ['DJANGO_SETTINGS_MODULE'] = 'mineria.settings'

class Command(BaseCommand):
    help = 'Inserta datos en la base de datos'

    def handle(self, *args, **options):
        # Aquí puedes insertar los datos que desees
        datos_minerales = [
            {'nombre': 'Sulfuros', 'lugar_extraccion': 'Lugar1', 'peso': 1.83, 'pureza': 0.38},
            {'nombre': 'Silicatos', 'lugar_extraccion': 'Lugar2', 'peso': 2.34, 'pureza': 0.97},
            {'nombre': 'Carbonatos', 'lugar_extraccion': 'Lugar2', 'peso': 2.34, 'pureza': 0.37},
            {'nombre': 'Sulfatos', 'lugar_extraccion': 'Lugar2', 'peso': 2.84, 'pureza': 0.37},
            {'nombre': 'Fosfatos', 'lugar_extraccion': 'Lugar2', 'peso': 2.34, 'pureza': 0.37},
            {'nombre': 'Óxidos e Hidróxidos', 'lugar_extraccion': 'Lugar2', 'peso': 2.74, 'pureza': 0.37},
            {'nombre': 'Haluros', 'lugar_extraccion': 'Lugar2', 'peso': 2.44, 'pureza': 0.97},
            {'nombre': 'arcillosos', 'lugar_extraccion': 'Lugar2', 'peso': 2.34, 'pureza': 0.27},
            {'nombre': 'Industriales', 'lugar_extraccion': 'Lugar2', 'peso': 2.34, 'pureza': 0.97},
            {'nombre': 'Metálicos', 'lugar_extraccion': 'Lugar2', 'peso': 2.14, 'pureza': 0.77},
            {'nombre': 'piedras', 'lugar_extraccion': 'Lugar2', 'peso': 2.74, 'pureza': 0.87},
            # Agrega más datos según sea necesario
        ]

        for dato in datos_minerales:
            mineral = Mineral(
                nombre=dato['nombre'],
                lugar_extraccion=dato['lugar_extraccion'],
                peso=dato['peso'],
                pureza=dato['pureza']
            )
            mineral.save()

        self.stdout.write(self.style.SUCCESS('Datos insertados exitosamente'))
