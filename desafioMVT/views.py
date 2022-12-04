from django.shortcuts import render
from django.template import Template,Context,loader
from .models import *
from django.http import HttpResponse

# Create your views here.
def familia(request):
    padre = Persona()
    padre.nombre="Ale"
    padre.apellido="Fruchdman"
    padre.rolFamiliar="Padre"
    padre.save()

    madre = Persona()
    madre.nombre="Jesica"
    madre.apellido="Todisco"
    madre.rolFamiliar="Madre"
    madre.save()

    hija = Persona()
    hija.nombre="Rebeca"
    hija.apellido="Fruchdman"
    hija.rolFamiliar="Hija"
    hija.save()

    myDic = {
        'padre':padre,
        'madre':madre,
        'hija':hija
        }
        
    mytemplate=loader.get_template("familia.html")
    miPagina= mytemplate.render(myDic)
    return HttpResponse(miPagina)
