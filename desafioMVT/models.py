from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    fechaNacimiento=models.DateField(auto_now_add=True)
    edad = models.IntegerField
    dni=models.IntegerField
    email=models.EmailField()
    rolFamiliar=models.CharField(max_length=255, default="")
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.rolFamiliar}".format()
