from django.shortcuts import render
from familiares.models import Familiares


def crear_familiar(request):
    familiar_nuevo_01 = Familiares.objects.create(nombre = "Gonzalo", apellido_01 = "De Amunátegui", apellido_02 = "Márquez", dni = 14300964, fecha_nacimiento = "1977-09-17", parentesco = "Yo", ahorros = 0, active = True)
    familiar_nuevo_02 = Familiares.objects.create(nombre = "Abenchara", apellido_01 = "Florido", apellido_02 = "Alonso", dni = 54085591, fecha_nacimiento = "1984-10-20", parentesco = "Cónyuge", ahorros = 1000, active = True)
    familiar_nuevo_03 = Familiares.objects.create(nombre = "Ainara", apellido_01 = "De Amunátegui", apellido_02 = "Florido", dni = 54583956, fecha_nacimiento = "2015-05-11", parentesco = "Hija", ahorros = 100, active = True)
    familiar_nuevo_04 = Familiares.objects.create(nombre = "Aitor", apellido_01 = "De Amunátegui", apellido_02 = "Florido", dni = 42894977, fecha_nacimiento = "2018-09-10", parentesco = "Hijo", ahorros = 25, active = True)
    familiar_nuevo_05 = Familiares.objects.create(nombre = "Dori", apellido_01 = "De Amunátegui", apellido_02 = "Florido", dni = 0, fecha_nacimiento = "2020-07-05", parentesco = "Mascota", ahorros = 0, active = False)

    my_context = {"familiar_nuevo_01" : familiar_nuevo_01, "familiar_nuevo_02" : familiar_nuevo_02, "familiar_nuevo_03": familiar_nuevo_03, "familiar_nuevo_04" : familiar_nuevo_04, "familiar_nuevo_05" : familiar_nuevo_05}
    return render(request, "home.html", context=my_context)


"""
def crear_familiar(request):
    familiar_nuevo = Familiares.objects.create(nombre = "Dori", apellido_01 = "De Amunátegui", apellido_02 = "Florido", dni = 14300964, fecha_nacimiento = "2020-07-05", parentesco = "Mascota", ahorros = 0, active = True)
    my_context = {"familiar_nuevo" : familiar_nuevo}
    return render(request, "home.html", context = my_context)
"""


def ver_familiares(request):
    familiar_mostrado = Familiares.objects.filter(active = True)
    # familiar_mostrado = Familiares.objects.all()
    # filter  = all + filter
    # exclude
    my_context = {"familiar_mostrado" : familiar_mostrado}
    return render(request, "ver_familiares.html", context = my_context)
