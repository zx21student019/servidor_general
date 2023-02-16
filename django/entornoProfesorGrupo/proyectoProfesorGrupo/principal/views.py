from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Profesor, Grupo

class profesoresListView(ListView):
     model = Profesor
     
class profesoresCreateView(CreateView):
     model = Profesor
     fields = ['nombre', 'apellidos', 'telefono', 'correo', 'asignatura']
     success_url = reverse_lazy('listado')

class profesoresUpdateView(UpdateView):
     model = Profesor
     fields = ['nombre', 'apellidos', 'telefono', 'correo', 'asignatura']
     template_name_suffix = '_update'
     success_url = reverse_lazy('listado')

class profesoresDeleteView(DeleteView):
     model = Profesor
     success_url = reverse_lazy('listado')
