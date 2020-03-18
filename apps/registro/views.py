from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate, get_user_model
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest    
from django.contrib import messages
# from django.views.generic import TemplateView
from apps.registro.forms import LoginForm, ParticipanteForm
from apps.registro.models import Empresas, Categoria, Estados, Participantes
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import  *
from django.urls import reverse


def index(request):
    if request.method== 'POST':
        busqueda = request.POST['search']
        fil = request.POST['nom']
        print(fil)
        words = busqueda.split()
        print(words)
        contador=0
        resultados=[] 
        stopwords = ['de', 'en', 'la', 'con', 'de', 'y', 'a', 'los','las', 'DE', 'EN', 'LA', 'CON', 'DE', 'Y', 'A', 'LOS','LAS']
        for word in list(words):  # iterating on a copy since removing will mess things up
            if word in stopwords:
                words.remove(word)

        print(words)
        if(busqueda):
            # Q(nombre__icontains=word) | Q(servicios__icontains=word) || 
            if(fil=="1"):
                resultados = Empresas.objects.filter(Q(nombre__unaccent__icontains=busqueda))
            if(fil=="2"):
                resultados = Empresas.objects.filter(Q(categoria__nombre__unaccent__icontains=busqueda))
            if(fil=="3"):
                resultados = Empresas.objects.filter(Q(categoria__nombre__unaccent__icontains=words[0]) & Q(municipio__unaccent__icontains=words[1]))
            
        if resultados:
            contador = resultados.count()
        else:
            contador=0
        if resultados: 
            return render(request, 'usuarios/resultados.html', {'resultados':resultados, 'contador': contador, 'busqueda': busqueda})      
        else:
            messages.error(request,'Resultados no encontrados')
            return render(request,'usuarios/resultados.html',{'contador': contador, 'busqueda': busqueda})  
    return render(request, 'index.html')


def resultados(request):
    return render(request, "usuarios/resultados.html")

def registro_view(request):
    estados = Estados.objects.all()
    if request.method=='POST':
        form = ParticipanteForm(request.POST or None, request.FILES or None)
        print(form.is_valid())
        if form.is_valid():
            part = form.save(commit=False)
            messages.success(request,"Registro con exito")
            part.save()
        return redirect("index")
    else:
        form = ParticipanteForm()
    return render(request, "usuarios/registro_participantes.html",{'estados': estados,'form': form})    

def listado_participantes(request):
    participantes = Participantes.objects.all().order_by('-num_votos')
    return render(request, "usuarios/listado_participantes.html",{'participantes':participantes})

def filtrado_dentistas(request):
    return render(request, "usuarios/filtrado_dentistas.html")

def filtrado_hoteles(request):
    return render(request, "usuarios/filtrado_hoteles.html")
    
def filtrado_agencias(request):
    return render(request, "usuarios/filtrado_agencias.html")

def filtrado_restaurantes(request):
    return render(request, "usuarios/filtrado_restaurantes.html")

def detalle(request, pk):
    try:
        empresa = Empresas.objects.get(pk=pk)
        json_lat = json.dumps(str(empresa.latitud))
        json_long = json.dumps(str(empresa.longitud))
    except empresa.DoesNotExist:
        raise Http404
    return render(request, "usuarios/detalle.html", {'empresa': empresa,'json_long':json_long,'json_lat':json_lat})

def filtro_estado_giro(request, pk_estado, pk_categoria):
    if request.method== 'GET':
        print(pk_estado)
        print(pk_categoria)
        empresas = Empresas.objects.filter(Q(estado_id=pk_estado) & Q(categoria__id=pk_categoria))
        print(empresas)
        if empresas:
            contador = empresas.count()
        else:
            contador=0
        if empresas: 
            return render(request, "usuarios/resultados_filtrado.html", {'empresas': empresas, 'contador': contador})     
        else:
            messages.error(request,'Resultados no encontrados')
            return render(request, "usuarios/resultados_filtrado.html", {'contador': contador})
    return render(request, 'index.html')
    
    # try: 
    #     print(pk_estado)
    #     print(pk_categoria)
    #     empresas = Empresas.objects.filter(Q(estado__contains=pk_estado) & Q(categoria__contains=pk_categoria))
    #     contador = empresas.count()
    # except empresas.DoesNotExist:
    #     raise Http404
    # return render(request, "usuarios/resultados_filtrado.html", {'empresas': empresas, 'contador': contador})



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
         "nombres":nombres
        }
        return Response(data)

# ciudades= []
#                 instan = Empresas.objects.all()
#                 for i in instan:
#                     ciudades.append(i.municipio.lower())

#                 for word in list(words):  # iterating on a copy since removing will mess things up
#                     if word in stopwords:
#                         words.remove(word)
                
#                 for city in list(ciudades):  # iterating on a copy since removing will mess things up
#                     if city.lower() in words:
#                         ciudad= city
#                         for w in list(words):  # iterating on a copy since removing will mess things up
#                             if w.lower() ==ciudad.lower():
#                                 words.remove(w)

#                         cate= " ".join(words)
#                         print(ciudad)
#                         print(cate)
#                         resultados = Empresas.objects.filter(Q(categoria__nombre__unaccent__icontains=cate) & Q(municipio__unaccent__icontains=ciudad))