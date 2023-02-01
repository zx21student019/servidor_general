from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    home = loader.get_template('recetario/inicio.html')
    return HttpResponse(home.render())

def receta(request):
    receta = loader.get_template('recetario/receta.html')
    return HttpResponse(receta.render())

def desayunos(request):
    desayunos = loader.get_template('recetario/desayunos.html')
    return HttpResponse(desayunos.render())

def comidas(request):
    comidas = loader.get_template('recetario/comidas.html')
    return HttpResponse(comidas.render())

def cenas(request):
    cenas = loader.get_template('recetario/cenas.html')
    return HttpResponse(cenas.render())

def todas(request):

    recetas = get_object_or_404(Receta)
    ctx = {
        'recetas':recetas,
    }

    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))

def categoria(request,idCategoria):
    recetas = get_list_or_404(receta,categoria=idCategoria)
    ctx = {
        'recetas':recetas,
    }

    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))

