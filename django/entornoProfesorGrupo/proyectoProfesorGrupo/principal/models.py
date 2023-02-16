from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profesor(models.Model):
    nombre  = models.CharField(max_length=200)
    apellidos  = models.CharField(max_length=200)
    telefono  = models.CharField(max_length=20,null=True)
    correo = models.EmailField()
    asignatura  = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')    

    class Meta:
        verbose_name='profesor'
        verbose_name_plural="profesores"
        ordering=['-created']

    def __str__(self):
        return self.nombre, self.apellidos

class Grupo(models.Model):
    curso = models.CharField(max_length=100)
    letra = models.CharField(max_length=10)
    descripcion = models.TextField(null=True)
    numAlumnos = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    profesor = models.ManyToManyField(Profesor,verbose_name="profesor")

    class Meta:
        verbose_name='grupo'
        verbose_name_plural="grupo"
        ordering=['-created']

    def __str__(self):
        return self.curso, self.letra 

