from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecetaListView.as_view(), name='listado'),
    path('receta/<int:pk>', views.RecetaDetailView.as_view(), name='detalle'),
    path('crear', views.RecetaCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>', views.RecetaUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>', views.RecetaDeleteView.as_view(), name='borrar'),    
]