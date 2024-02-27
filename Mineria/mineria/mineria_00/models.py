from django.db import models

# Create your models here.

class Mineral(models.Model):#1
    nombre = models.CharField(max_length=200, blank=False)
    lugar_extraccion = models.CharField(max_length=200, blank=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    pureza = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    
    class Meta:
        db_table = 'Mineral'
        verbose_name = 'Mineral'
        verbose_name_plural  = 'Minerales'
        
    def __str__(self):                 
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("Mineral", kwargs={"pk": self.pk})
    