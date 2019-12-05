from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate, get_user_model
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest    
from django.contrib import messages
from django.views.generic import TemplateView
from apps.registro.forms import LoginForm
from apps.registro.models import Empresas, Categoria
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import  *
# Create your views here.

def index(request):
    if request.method== 'POST':
        busqueda = request.POST['search']
        words = busqueda.split()
        resultados = Empresas.objects.all()
        for word in words:
            resultados = resultados.filter(Q(nombre__icontains=word) | Q(servicios__icontains=word) | Q(categoria__nombre__icontains=word) | Q(estado__nombre__icontains=word) | Q(municipio__icontains=word))
            pass
        contador = resultados.count()
        if resultados: 
                return render(request, 'usuarios/resultados.html', {'resultados':resultados, 'contador': contador, 'busqueda': busqueda})      
        else:
            messages.error(request,'Resultados no encontrados') 
            return HttpResponseRedirect('index')   
    return render(request, 'index.html')


def resultados(request):
    resultados = Empresas.objects.all()
    contador = Empresas.objects.all().count()
    context = {
        'resultados':resultados,
        'contador': contador
    }
    return render(request, "usuarios/resultados.html", context)

@login_required(login_url='/login/')
def vista_logout(request):
    logout(request)
    return redirect('index')


def vista_login(request):
    form  = LoginForm(request.POST or None)
    context = {"form":form}
    if request.user.is_authenticated:
        return redirect('index')
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,"usuarios/login.html",context)

class CharData(APIView):

    def get(self, request, format=None):
        #Nombres-Empresa
        nombres= []
        instance = Empresas.objects.all()
        for i in instance:
            nombres.append(i.nombre)

        
        data ={
         "nombre":nombres
        }
        return Response(data)
