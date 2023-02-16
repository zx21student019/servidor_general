from django.contrib import admin

from .models import Profesor, Grupo

class GrupoAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')
     list_display=('curso', 'letra', 'numAlumnos')
     ordering = ('curso', 'letra')
     
class ProfesorAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')
     list_display = ('apellidos','nombre', 'asignatura')
     ordering = ('apellidos', 'nombre')

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Grupo)