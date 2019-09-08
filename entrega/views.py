from django.shortcuts import render
from .models import *
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    
    context={}
    return render(request, 'index.html', context)

def convocatoria(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'convocatoria.html', context)

def registro(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'registro.html', context)

@login_required(login_url='/')
def entrega(request):
    #buscador de estudiantes
    try:
        busqueda = request.GET['busqueda']        
    except:
        busqueda = False
   # entregado = Entrega.objects.all()
    estudiante = Estudiante.objects.filter( Q(user__username__icontains=busqueda) |
                                       Q(user__first_name__icontains=busqueda)|Q(user__last_name__icontains=busqueda)

    )
    #aca valido si la busqueda arroja un solo resultado que redirecciones autamaticamente    
    if len(estudiante)==1:
        obj = estudiante.latest('pk')
        print(obj)
        return HttpResponseRedirect('/entrega/?id='+str(obj.pk))    
    try:
        cod = request.GET['id']        
    except:
        cod = False  
    #Escojer estudiantes
    try:
        estudiante_result = Estudiante.objects.get(pk=int(cod))
    except:
        estudiante_result = False
    try:
        beneficio = Beneficiario.objects.filter(estudiante_id=cod)
    except:
        beneficio = False    
    context={'estudiante':estudiante,'estudiante_result':estudiante_result,'beneficio':beneficio}
    return render(request, 'entrega.html', context)

def perfil(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'perfil.html', context)

def configuracion(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'configuracion.html', context)