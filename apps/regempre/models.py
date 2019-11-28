from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=60, blank=False, help_text="Aquí ingresa el nombre de la empresa")
    email = models.EmailField(help_text="Aquí ingresa el email de la empresa")
    telefono = models.CharField(max_length=15, blank=False, help_text="Aquí ingresa el teléfono de la empresa")
    servicios = models.TextField(max_length=200, blank=False, help_text="Aquí ingresa los servicios de la empresa")
    imagen = models.ImageField()
    red_social = models.CharField(max_length=200, blank=False, help_text="Aquí ingresa la red social de la empresa")
    direccion = models.CharField(max_length=200, blank=False, help_text="Aquí ingresa la dirección de la empresa")
    latitud = models.DecimalField(max_digits=50, decimal_places=20, blank=False)
    longitud = models.DecimalField(max_digits=50, decimal_places=20, blank=False)

    def __str__(self):
        return self.nombre


