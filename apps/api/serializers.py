from rest_framework import serializers
from apps.registro.models import Empresas
from django.db import models

#En esta clase se serializan los eventos
class EmpresaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Empresas
        fields = ['nombre']