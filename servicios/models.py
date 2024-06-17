from django.db import models

# Create your models here.

class Servicio(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='servicios', default='default.jpg')
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion[:50]
    
    class Meta:
        verbose_name_plural = "Servicios"