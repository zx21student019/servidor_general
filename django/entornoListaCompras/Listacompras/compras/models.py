from django.db import models

class compras(models.Model):
    producto = models.CharField(max_length=255)
    cantidad = models.FloatField()
    unidad = models.CharField(max_length=255)
    comprado = models.BooleanField()