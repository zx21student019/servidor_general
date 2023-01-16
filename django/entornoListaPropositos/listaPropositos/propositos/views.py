from django.shortcuts import render
from django.http import HttpResponse
from .models import Proposito

def listadoPropositos(request):
    propositos = Proposito.objects.all()
    contexto = {
        "propositos": propositos
    }
    return render(request,"propositos.html",contexto)

#def anadirPropositos(request):
#    nuevoProposito=Proposito(proposito,)
    
