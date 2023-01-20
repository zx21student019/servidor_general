from django.urls import include, path

from . import views

app_name = 'propositos'

urlpatterns = [
    path('', views.listadoPropositos, name='listadoPropositos'),
    path('anadir/', views.anadirProposito, name='anadirProposito'),
    path('borrar/<int:id>', views.borrarProposito, name='borrarProposito'),
    path('modificar/<int:id>', views.modificarProposito, name='modificarProposito'),
    path('guardar/<int:id>', views.guardarProposito, name='guardarProposito'),
    path('completar/<int:id>', views.completarProposito, name='completarProposito'),
    path('resetear/<int:id>', views.resetearProposito, name='resetearProposito'),
]
