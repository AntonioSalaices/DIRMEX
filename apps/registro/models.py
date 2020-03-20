from django.db import models
from datetime import datetime
# Create your models here.

class Estados(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class Empresas(models.Model):
    nombre = models.CharField(max_length=70,  help_text="Aquí ingresa el nombre de la empresa", verbose_name="Nombre")
    email = models.EmailField(help_text="Aquí ingresa el email de la empresa", blank=True)
    telefono = models.CharField(max_length=30, help_text="Aquí ingresa el teléfono de la empresa",verbose_name="Teléfono" )
    servicios = models.TextField(max_length=300,help_text="Aquí ingresa los servicios de la empresa")
    imagen = models.ImageField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, verbose_name="Categoría")
    red_social = models.CharField(max_length=200, blank=True, help_text="Aquí ingresa la red social de la empresa")
    cp = models.CharField(max_length=10,  help_text="Código Postal", verbose_name="Código Postal")
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE)
    municipio = models.CharField(max_length=30,  help_text="Municipio")
    colonia = models.CharField(max_length=20,  help_text="Colonia")
    calle = models.TextField(max_length=200,  help_text="Calle")
    noext = models.CharField(max_length=30,  help_text="No. Exterior", verbose_name="No. Exterior")
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return str(self.id)+ '.- ' + self.nombre


class Participantes(models.Model):
    nombre = models.CharField(max_length=100,  help_text="Aquí ingresa el nombre", verbose_name="Nombre", blank=True)
    telefono = models.CharField(max_length=30, unique=True, help_text="Aquí ingresa el teléfono",verbose_name="Teléfono", blank=True)
    telefono2 = models.CharField(max_length=30, help_text="Aquí ingresa el teléfono 2",verbose_name="Teléfono 2", blank=True)
    email = models.EmailField(help_text="Aquí ingresa el email del participante", blank=True)
    imagen = models.ImageField(blank=True)
    red_social = models.CharField(max_length=200, blank=True, help_text="Aquí ingresa su red social")
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE)
    municipio = models.CharField(max_length=30,  help_text="Municipio", blank=True)
    colonia = models.CharField(max_length=20,  help_text="Colonia", blank=True)
    num_votos = models.IntegerField(default=0,blank=True)

    class Meta:
        verbose_name = 'participante'
        verbose_name_plural = 'participantes'

    def __str__(self):
        return str(self.id)+ '.- ' + self.nombre
