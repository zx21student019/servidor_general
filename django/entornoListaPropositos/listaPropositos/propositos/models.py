from django.db import models

# Create your models here.
class Proposito(models.Model):
    proposito = models.CharField(max_length=256)
    fechaObjetivo = models.DateField()
    completado = models.BooleanField(null=True)
    fechaCompletado =models.DateField(null=True)