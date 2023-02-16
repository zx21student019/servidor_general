from django.urls import path
from . import views

urlpatterns = [
    path('', views.profesoresListView.as_view(), name='listado'),
    path('crear', views.profesoresCreateView.as_view(), name='crear'),
    path('modificaProfesor/<int:pk>', views.profesoresUpdateView.as_view(), name='profesorModificar'),
    path('borrar/<int:pk>', views.profesoresDeleteView.as_view(), name='borraProfesor'),    
]