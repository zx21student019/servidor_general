from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Receta, Categorias

class RecetaListView(ListView):
     model = Receta
     
class RecetaDetailView(DetailView):
     model = Receta
     
class RecetaCreateView(CreateView):
     model = Receta
     fields = ['nombre', 'subnombre', 'imagen', 'ingredientes', 'receta', 'author', 'categorias']
     success_url = reverse_lazy('listado')

class RecetaUpdateView(UpdateView):
     model = Receta
     fields = ['nombre', 'subnombre', 'imagen', 'ingredientes', 'receta', 'categorias']
     template_name_suffix = '_update'
     success_url = reverse_lazy('listado')

class RecetaDeleteView(DeleteView):
     model = Receta
     success_url = reverse_lazy('listado')


# def inicio(request):
#     home = loader.get_template('recetario/inicio.html')
#     return HttpResponse(home.render())

# def receta(request):
#     receta = loader.get_template('recetario/receta.html')
#     return HttpResponse(receta.render())

# def desayunos(request):
#     desayunos = loader.get_template('recetario/desayunos.html')
#     return HttpResponse(desayunos.render())

# def comidas(request):
#     comidas = loader.get_template('recetario/comidas.html')
#     return HttpResponse(comidas.render())

# def cenas(request):
#     cenas = loader.get_template('recetario/cenas.html')
#     return HttpResponse(cenas.render())

# def todas(request):
#     recetas = get_list_or_404(Receta)
#     contexto = {
#         'recetas': recetas,
#     }
#     todas = loader.get_template('recetario/todas.html')
    
#     return HttpResponse(todas.render(contexto, request))

# def categoria(request, id_categoria):
#     recetas = get_list_or_404(Receta, categorias=id_categoria)
#     contexto = {
#         'recetas': recetas,
#     }
#     todas = loader.get_template('recetario/todas.html')
    
#     return HttpResponse(todas.render(contexto, request))