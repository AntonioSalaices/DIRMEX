from rest_framework import generics
from apps.registro.models import Empresas
from apps.api.serializers import EmpresaSerializer
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

class ListEmpresasAPI(generics.ListAPIView):
    queryset = Empresas.objects.all() #Consulta ORM que devuelve los productos
    serializer_class = EmpresaSerializer #Metodo para serializar los campos del modelo
    filter_backends = [filters.SearchFilter] #Implementación del filtro
    search_fields = ['nombre']  # Aquí se determinan los filtros posibles     
    
