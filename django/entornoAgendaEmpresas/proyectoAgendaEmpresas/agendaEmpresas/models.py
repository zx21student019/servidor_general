from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    tipo = models.CharField(max_length=255, verbose_name="tipo")
    direccion = models.CharField(max_length=255, verbose_name="direccion")
    telefono = models.CharField(max_length=255, verbose_name="telefono")
    personaContacto = models.CharField(max_length=255, verbose_name="persona de contacto")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de modificacion")

    def __str__(self):
        return self.nombre