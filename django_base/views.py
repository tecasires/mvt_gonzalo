from django.http import HttpResponse
from django.shortcuts import render


def my_home(request):
    my_context = {}
    return render(request, "home.html", context = my_context)


def my_view(request):
    return HttpResponse("View")


def my_template(request):
    my_context = {}
    return render(request, "template.html", context = my_context)
