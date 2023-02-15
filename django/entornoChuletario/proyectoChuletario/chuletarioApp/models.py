from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(verbose_name='foto persona',upload_to='ventaPersonas')
    fechaCreacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)