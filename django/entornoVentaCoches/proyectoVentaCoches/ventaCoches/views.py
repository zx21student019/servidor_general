from django.shortcuts import render
from .models import Coche
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def ventaCoches(request):
    ventCoch = Coche.objects.all() 
    contexto = {
        'listCoch':ventCoch,
    }
    plantilla = loader.get_template('ventaCoches.html')
    return HttpResponse(plantilla.render(contexto,request))