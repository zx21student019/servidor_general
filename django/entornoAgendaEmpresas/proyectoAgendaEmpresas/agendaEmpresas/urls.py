from django.urls import path
from .views import EmpresaListView, EmpresaDetailView,EmpresaCreateView,EmpresaDeleteView,EmpresaUpdateView

urlpatterns = [
    path('',EmpresaListView.as_view(), name='listado'),
    path('crearEmpresa',EmpresaCreateView.as_view(), name='crear'),
    path('agendaEmpresa/<int:pk>',EmpresaDetailView.as_view(), name='detalle'),
    path('borrarEmpresa/<int:pk>',EmpresaDeleteView.as_view(), name='borrar'),
    path('modificarEmpresa/<int:pk>',EmpresaUpdateView.as_view(), name='modificar'),
]