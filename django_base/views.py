from django.http import HttpResponse
from django.shortcuts import render


def mi_vista(request):
    return HttpResponse("Vista")


def mi_template(request):
    mi_contexto = {}
    return render(request, "template_01.html", context = mi_contexto)


def mi_inicio(request):
    mi_contexto = {}
    return render(request, "inicio.html", context = mi_contexto)
