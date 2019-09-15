from django.shortcuts import render
from .models import *
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Value as V
from django.db.models.functions import Concat  
from datetime import datetime, date, time, timedelta
# Create your views here.
def home(request):
#<<<<<<< HEAD
#=======
    
#>>>>>>> c4972948245d3e0bebd994fddb92ac8b910f1519
    mes5=(datetime.now() - timedelta(days=0)).strftime('%B')
    mes4=(datetime.now() - timedelta(days=30)).strftime('%B') 
    mes3=(datetime.now() - timedelta(days=60)).strftime('%B') 
    mes2=(datetime.now() - timedelta(days=90)).strftime('%B') 
    mes1=(datetime.now() - timedelta(days=120)).strftime('%B') 
    
    dia7 = (datetime.now() - timedelta(days=6)).strftime('Día: %a')
    dia6 = (datetime.now() - timedelta(days=5)).strftime('Día: %a')
    dia5 = (datetime.now() - timedelta(days=4)).strftime('Día: %a')
    dia4 = (datetime.now() - timedelta(days=3)).strftime('Día: %a')
    dia3 = (datetime.now() - timedelta(days=2)).strftime('Día: %a')
    dia2 = (datetime.now() - timedelta(days=1)).strftime('Día: %a')
    dia1 = (datetime.now() - timedelta(days=0)).strftime('Día: %a')
    context={'dia7': dia7,
             'dia6': dia6,
             'dia5': dia5,
             'dia4': dia4,
             'dia3': dia3,
             'dia2': dia2,
             'dia1': dia1,
             'mes5': mes5,
             'mes4': mes4,
             'mes3': mes3,
             'mes2': mes2,
             'mes1': mes1,
             }
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
    queryset = Estudiante.objects.annotate(fullname=Concat('user__first_name', V(' '), 'user__last_name'))
    estudiante = queryset.filter( Q(user__username__icontains=busqueda) |                                      
                                       Q(fullname__icontains=busqueda)

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

def refrigerio(request):
    context={}
    return render(request, 'refrigerio.html', context)

def almuerzo(request):

    context={}

    return render(request, 'almuerzo.html', context)