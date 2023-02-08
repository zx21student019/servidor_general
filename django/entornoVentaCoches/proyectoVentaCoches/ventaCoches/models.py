from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    fechaModificacion = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')    

    class Meta:
        verbose_name='categoria'
        verbose_name_plural="categorias"
        ordering=['-fechaCreacion']

    def __str__(self):
        return self.nombre

class Coche(models.Model):
    marca = models.CharField(max_length=200)
    modelo  = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(verbose_name='foto coche',upload_to='ventaCoches')
    fechaCreacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='coche'
        verbose_name_plural="coches"
        ordering=['-fechaCreacion']

    def __str__(self):
        return self.nombre 
