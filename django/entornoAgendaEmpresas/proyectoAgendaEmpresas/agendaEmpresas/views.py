from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Empresa
from django.views.generic import ListView, DetailView



# Create your views here.
class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa


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