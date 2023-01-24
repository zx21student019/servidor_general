from django.db import models
from django.contrib.auth.models import User
from datetime.

class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    subnombre = models.CharField(max_length=255, null=True)
    imagen = models.ImageField(verbose_name='foto receta',upload_to='resetario')
    ingredientes = models.TextField(null=True)
    receta = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion',default=now)
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)

    class Meta:
        verbose_name='receta'
        verbose_name_plural="recetas"
        ordering=[]

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)