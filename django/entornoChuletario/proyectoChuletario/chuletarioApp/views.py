from django.shortcuts import render
from .models import Persona
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def chuletarioApp(request):
    na = Persona.objects.all() 
    contexto = {
        'ln':na,
    }
    plantilla = loader.get_template('chuletario.html')
    return HttpResponse(plantilla.render(contexto,request))