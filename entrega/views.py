from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from datetime import *
import itertools
# Create your views here.

def login(request):
    error=False
    beneficio_list = Tipo_beneficio.objects.all()
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        beneficio = request.POST['beneficio']
        if beneficio == 'admin':
            try:
                user_admin = User.objects.get(username=username)
            except:
                user_admin = False
                error = 'Ingrese un Usuario Valido'
            if user_admin and user_admin.is_superuser:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error = 'Contraseña Erronea o este usuario no es administrador'
            else:
                error = 'Este usuario no es administrador'
        try:
            personal = Personal.objects.get(user__username=username)
            try:
                acceso = Acceso_Modulo.objects.get(personal_id=personal.pk,modulo__tipo_beneficio_id=int(beneficio))
                user = authenticate(username=username, password=password)
                if user is not None:
                    request.session['modulo'] = acceso.modulo.tipo_beneficio.nombre
                    request.session['modulo_id'] = acceso.modulo.tipo_beneficio.id
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error = 'Usuario contraseña Incorrecta'
            except:
                acceso = False
                error = 'Este Usuario no tiene permisos para este modulo'
        except:
            personal = False
            error = 'Este usuario no es un personal autorizado'
        print(username,password,beneficio_list)
    context={'beneficio_list':beneficio_list,'error':error}
    return render(request, 'registration/login.html', context)

def home(request):
    fecha = date.today()
    start_week = fecha - timedelta(fecha.weekday())
    end_week = start_week + timedelta(7)
    asistencia = Asistencia.objects.filter(fecha__range=[start_week, end_week])

    qs = asistencia.values('fecha').values('fecha')
    grouped = itertools.groupby(qs, lambda d: d.get('fecha').strftime('%Y-%m-%d'))
    [(day, len(list(this_day))) for day, this_day in grouped]

    context={'asistencia':asistencia}
    return render(request, 'index.html', context)

def convocatoria(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'convocatoria.html', context)

def registro(request):
    if request.method == 'POST':
        formuser = UsuarioForm(request.POST, request.FILES)
        formpersonal = ProfileForm(request.POST, request.FILES)

        if formuser.is_valid():
            user = formuser.save(commit=False)
            user.username = user.email
            user_password = user.password
            user.set_password(user_password)
            user.save()
            return HttpResponseRedirect('/registro/')
        if formpersonal.is_valid():
            Personal = formpersonal.save(comit=False)
            Personal.user = user
            Personal.save()
            return HttpResponseRedirect('/registro/')
    else:
        formuser = UsuarioForm()
        formpersonal = ProfileForm()

    context={'formuser': formuser, 'formpersonal': formpersonal}

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
    #verificamos el acceso del personal al modulo
    try:
        acceso = Acceso_Modulo.objects.get(personal__user_id=request.user.id,modulo__tipo_beneficio_id=int(request.session['modulo_id']))
    except:
        acceso = False
    #verificcamos si ya el estudiante recibio el beneficio
    try:
        beneficio_est = Beneficiario.objects.get(estudiante_id=cod,tipo_beneficio_id=int(request.session['modulo_id']))
        asistencia = Asistencia.objects.get(beneficiario_id=beneficio_est.id,fecha__date=date.today())
        print('beneficiado')
    except:
        beneficio_est = False
        asistencia = False
    context={'estudiante':estudiante,'estudiante_result':estudiante_result,'beneficio':beneficio,'acceso':acceso,'asistencia':asistencia}
    return render(request, 'entrega.html', context)
def asistencia(request,id):
    try:
        acceso = Acceso_Modulo.objects.get(personal__user_id=request.user.id,modulo__tipo_beneficio_id=int(request.session['modulo_id']))
    except:
        acceso = False
    asistencia = Asistencia.objects.create(beneficiario=Beneficiario.objects.get(pk=id),acceso_modulo=acceso)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def perfil(request):
    print(request.user.id)
    try:
        perfil = Personal.objects.get(user__pk=request.user.id)
    except:
        perfil = False

    # entregado = Entrega.objects.all()
    context={'perfil':perfil}
    return render(request, 'perfil.html', context)

def configuracion(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'configuracion.html', context)