from django.db import models

# Create your models here.

class Transporte(models.Model):#2 
    matricula = models.CharField(max_length=200)
    tipo_transporte = models.CharField(max_length=200)
    capacidad_carga = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_mantenimiento = models.DateField()
    
    class Meta:
        db_table = 'Transporte'
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'
    
    def __str__(self):                 
        return self.matricula
    
    def get_absolute_url(self):
        return reverse("Transporte", kwargs={"pk": self.pk})
    