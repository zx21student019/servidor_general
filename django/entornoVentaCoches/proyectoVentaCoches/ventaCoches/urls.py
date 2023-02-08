from django.urls import path
from . import views

urlpatterns = [
    path('', views.CocheListView.as_view(), name='listado'),
    path('ventaCoches/<int:pk>', views.CocheDetailView.as_view(), name='detalle'),
    path('crear', views.CocheCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>', views.CocheUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>', views.CocheDeleteView.as_view(), name='borrar'),    
]