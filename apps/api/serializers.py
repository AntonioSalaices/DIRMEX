from rest_framework import serializers
from apps.regempre.models import Registro
from django.db import models

#En esta clase se serializan los eventos
class EmpresaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Registro
        fields = '__all__'