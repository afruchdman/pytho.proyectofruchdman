from django.shortcuts import render
from django.template import Template,Context,loader
from .models import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
      return render(request, "index.html")
      
def familia(request):
    padre = Persona()
    padre.nombre="Ale"
    padre.apellido="Fruchdman"
    padre.rolFamiliar="Padre"
    padre.edad = 51
    padre.save()

    madre = Persona()
    madre.nombre="Jesica"
    madre.apellido="Todisco"
    madre.edad = 39
    madre.rolFamiliar="Madre"
    madre.save()

    hija = Persona()
    hija.nombre="Beky"
    hija.apellido="Fruchdman"
    hija.edad = 6
    hija.rolFamiliar="Hija"
    hija.save()

        
    return render(request, 'familia.html', {"myDic":(padre,madre,hija)})

