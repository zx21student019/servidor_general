from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Proposito

def listadoPropositos(request):
    propositos = Proposito.objects.all()
    contexto = {
        "propositos": propositos
    }
    return render(request,'propositos.html',contexto)

def anadirProposito(request):
    nuevoProposito = Proposito(
        proposito=request.POST['nomProposito'],
        fechaObjetivo=request.POST['fechObjetivo']
    )
    nuevoProposito.save()
    return HttpResponseRedirect(reverse('propositos:listadoPropositos'))

def borrarProposito(request,id):
    proposito = Proposito.objects.get(pk=id)
    proposito.delete()
    return HttpResponseRedirect(reverse('propositos:listadoPropositos'))

def modificarProposito(request,id):
    proposito = Proposito.objects.get(pk=id)
    contexto = {
        "proposito": proposito
    }
    return render(request,'modificarPropositos.html',contexto)

def guardarProposito(request,id):
    proposito = Proposito.objects.get(pk=id)

    proposito.proposito=request.POST['nombProposito']
    proposito.fechaObjetivo=request.POST['fechaObjetivo']
    
    proposito.save()
    
    return HttpResponseRedirect(reverse('propositos:listadoPropositos'))


def completarProposito(request,id):
    proposito = Proposito.objects.get(pk=id)
    proposito.completado = True
    proposito.save()
    return HttpResponseRedirect(reverse('propositos:listadoPropositos'))

def resetearProposito(request,id):
    proposito = Proposito.objects.get(pk=id)
    proposito.completado = False
    proposito.save()
    return HttpResponseRedirect(reverse('propositos:listadoPropositos'))