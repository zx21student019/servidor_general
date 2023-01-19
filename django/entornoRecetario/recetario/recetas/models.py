from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    subnombre = models.CharField(max_length=255, null=True)
    imagen = models.CharField(max_length=255, null=True)
    ingredientes = models.TextField(null=True)
    receta = models.TextField(null=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)