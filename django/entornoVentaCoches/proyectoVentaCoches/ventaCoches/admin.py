from django.contrib import admin

from .models import Coche, Categorias

class CocheAdmin(admin.ModelAdmin):
     readonly_fields=('fechaCreacion')
     list_display=('marca', 'modelo')
     ordering = ('marca', 'modelo')
     search_fields = ('marca', 'modelo', 'author__username', 'categorias__nombre')
     date_hierarchy = ('fechaCreacion')
     
class CategoriasAdmin(admin.ModelAdmin):
     readonly_fields=('fechaCreacion', 'fechaModificacion')
     list_display = ('nombre', 'descripcion')

admin.site.register(Coche, CocheAdmin)
admin.site.register(Categorias)