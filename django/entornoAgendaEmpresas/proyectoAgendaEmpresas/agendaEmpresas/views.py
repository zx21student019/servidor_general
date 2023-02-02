from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Empresa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy



# Create your views here.
class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    fields=['nombre','tipo','direccion','telefono','personaContacto']
    reverse_lazy('listado')
    def get_success_url(self):
        return reverse('listado')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields=['nombre','tipo','direccion','telefono','personaContacto']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('listado')

'''
def listado(request):
    #modelo
    empresas = get_list_or_404(Empresa)
    #contexto
    ctx = {
        'empresa' :empresas,
    }
    #template
    listadoHTML = loader.get_template('agendaEmpresas/listado.html')
    #return template
    return HttpResponse(listadoHTML.render(ctx,request))
    '''