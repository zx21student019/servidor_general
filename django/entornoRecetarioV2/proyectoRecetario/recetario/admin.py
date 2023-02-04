from django.contrib import admin

# Register your models here.
from .models import Receta, Categorias

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields=('crecated','updated')
    list_display=('nombre','subnombre','author')
    ordering=('nombre','author')
    search_fields=('nombre',)

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','descripcion')

admin.site.register(Receta)
admin.site.register(Categorias)