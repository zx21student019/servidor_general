from django.db import models

# Create your models here.

class Coche(models.Model):
    marca = models.CharField(max_length=200)
    modelo  = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(verbose_name='foto coche',upload_to='ventaCoches')
    fechaCreacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
