from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    fechaNacimiento=models.DateField(auto_now_add=True)
    dni=models.IntegerField
    email=models.EmailField()
    rolFamiliar=models.CharField(max_length=255, default="")
