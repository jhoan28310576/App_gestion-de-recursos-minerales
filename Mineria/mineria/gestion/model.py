from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class gestion(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='gestion_img')
    
    class Meta:
        db_table = 'gestion'
        verbose_name = 'gestion'
        verbose_name_plural = 'gestiones'
        
    def __str__(self):                 
        return self.title
        
    def get_absolute_url(self):
        return reverse("gestion", kwargs={"pk": self.pk})