from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Coche

class CocheListView(ListView):
     model = Coche
     
class CocheDetailView(DetailView):
     model = Coche
     
class CocheCreateView(CreateView):
     model = Coche
     fields = ['marca', 'modelo', 'precio', 'descripcion', 'imagen', 'fechaCreacion', 'author']
     success_url = reverse_lazy('listado')

class CocheUpdateView(UpdateView):
     model = Coche
     fields = ['marca', 'modelo', 'precio', 'descripcion', 'imagen']
     template_name_suffix = '_update'
     success_url = reverse_lazy('listado')

class CocheDeleteView(DeleteView):
     model = Coche
     success_url = reverse_lazy('listado')