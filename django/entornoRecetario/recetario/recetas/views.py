from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    home = loader.get_template('inicio.html')
    return HttpResponse(home.render(request))

def receta(request):
    receta = loader.get_template('receta.html')
    return HttpResponse(home.render(request))
