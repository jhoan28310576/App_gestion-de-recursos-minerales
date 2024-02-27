from django.db import models


# Create your models here.

class Destino(models.Model):#3
    estado = models.CharField(max_length=200, blank=False)
    ciudad = models.CharField(max_length=200, blank=False)
    direccion = models.CharField(max_length=200, blank=False)
    class Meta:
        db_table = 'Destino'
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
    
    def __str__(self):                 
        return self.estado
    
    def get_absolute_url(self):
        return reverse("Destino", kwargs={"pk": self.pk})