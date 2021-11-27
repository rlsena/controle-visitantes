from visitantes.models import Visitante
from django.shortcuts import render

# Create your views here.

def index(request):

    todos_visitantes=Visitante.objects.all()

    context = {
        "nome_pagina":"Início da Dashboard",
        "todos_visitantes": todos_visitantes,
    }

    return render(request, "index.html", context)