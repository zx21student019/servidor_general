from django.urls import path
from .views import EmpresaListView, EmpresaDetailView

urlpatterns = [
    path('',EmpresaListView.as_view(), name='listado'),
    path('<int:pk>',EmpresaDetailView.as_view(), name='detalle'),
]