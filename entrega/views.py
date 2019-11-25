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
from django.db.models.functions import TruncDay,TruncMonth 
# Create your views here.

def login(request):
    error=False
    beneficio_list = Tipo_beneficio.objects.all()
    sede_list = Sede.objects.all()
    if request.method == 'POST':        
        username = request.POST['username']
        password = request.POST['password']
        beneficio = request.POST['beneficio']
        try:
            sede = request.POST['beneficio']
        except:
            sede = False 
        print(beneficio)

        if beneficio == 'estudiante':
            try:
                estudiante = Estudiante.objects.get(user__username=username)
                print('Entre esta vaina')
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    request.session['modulo'] = 'estudiante'
                    return HttpResponseRedirect('/perfilEstudiante/')
                else:
                    error = 'Contraseña Erronea o este usuario'

            except:
                error = 'Ingrese un Usuario Valido'
            
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
                    request.session['sede'] = sede
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

    context={'beneficio_list':beneficio_list,'error':error,'sede':sede_list}
    return render(request, 'registration/login.html', context)

def home(request):
    try:
        cantidad_refrigerio = Cantidad_semanal.objects.filter(tipo_beneficio__nombre='REFRIGERIO')
    except:
        cantidad = False
    fecha = date.today()
    start_week = fecha - timedelta(fecha.weekday())
    end_week = start_week + timedelta(7)
    asistencia_refrigerio= Asistencia.objects.filter(fecha__range=[start_week, end_week],beneficiario__tipo_beneficio__nombre='REFRIGERIO').annotate(day=TruncDay('fecha')).values("day").order_by().annotate(count=Count("id"))

    try:
        cantidad_almuerzo = Cantidad_semanal.objects.filter(tipo_beneficio__nombre='ALMUERZO')
    except:
        cantidad = False
    fecha = date.today()
    start_week = fecha - timedelta(fecha.weekday())
    end_week = start_week + timedelta(7)
    asistencia_almuerzo= Asistencia.objects.filter(fecha__range=[start_week, end_week],beneficiario__tipo_beneficio__nombre='ALMUERZO').annotate(day=TruncDay('fecha')).values("day").order_by().annotate(count=Count("id"))


    asistencia_total= Asistencia.objects.all().annotate(month=TruncMonth('fecha')).values("month").order_by().annotate(count=Count("id"))




    context={'asistencia_refrigerio':asistencia_refrigerio,'cantidad_refrigerio':cantidad_refrigerio,'cantidad_almuerzo':cantidad_almuerzo,'asistencia_almuerzo':asistencia_almuerzo,'asistencia_total':asistencia_total}
    return render(request, 'index.html', context)

def convocatoria(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'convocatoria.html', context)

def registro(request):
    if request.method == 'POST':
        formuser = UsuarioForm(request.POST, request.FILES)
        formpersonal = ProfileForm(request.POST, request.FILES)

        if formuser.is_valid() and  formpersonal.is_valid():
            user = formuser.save(commit=False)
            user.username = user.email
            user_password = user.password
            user.set_password(user_password)
                   
            try:
                user.save() 
                personal = formpersonal.save(commit=False)
                personal.user = user
                personal.save()
                return HttpResponseRedirect('/')
            except:
                print('Hubo un error')
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

    try:
        falla = Falla.objects.get(estudiante_id=int(cod))
    except:
        falla = False
      
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
    context={'estudiante':estudiante,'estudiante_result':estudiante_result,'beneficio':beneficio,'acceso':acceso,'asistencia':asistencia,'falla':falla}
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

def estudiantes_registrados(request):
    registro = Registro_estudiante.objects.filter(estado='PRESELECCION').order_by('estudiante__estrato','estudiante__pension_ud','estudiante__pension_de','estudiante__jovenes_accion','estudiante__deportista',)
    cantidad_semanal = Cantidad_semanal.objects.all().last()
    beneficiario = Beneficiario.objects.all()
    lunes = beneficiario.filter(lunes=True).count()
    martes = beneficiario.filter(martes=True).count()
    miercoles = beneficiario.filter(miercoles=True).count()
    jueves = beneficiario.filter(jueves=True).count()
    viernes = beneficiario.filter(viernes=True).count()
    total = lunes+martes+miercoles+jueves+viernes

    print(lunes,martes,miercoles,jueves,viernes)
    lista = ()
    
    if request.method == 'POST':
        print('entre')
        
        options = request.POST.getlist('options')
        if not options:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        

        my_filter_qs = Q()
        for x in options:
            my_filter_qs = my_filter_qs | Q(id=int(x))
            registro_estudiante = Registro_estudiante.objects.filter(my_filter_qs)
            registro_estudiante.filter(estado='PRESELECCION').order_by('estudiante__estrato','estudiante__pension_ud','estudiante__pension_de','estudiante__jovenes_accion','estudiante__deportista',)
        
        for x in registro_estudiante:
            validar = beneficiario.filter(estudiante=x.estudiante.id,tipo_beneficio__nombre=x.tipo_beneficio)
        
        if not validar:
            for x in registro_estudiante:
                tipo_beneficio = Tipo_beneficio.objects.get(nombre=x.tipo_beneficio)
                convocatoria = Convocatoria.objects.all().last()
                obj = Beneficiario.objects.create(estudiante=x.estudiante,tipo_beneficio=tipo_beneficio,convocatoria=convocatoria,sede=Sede.objects.get(sede=x.sede))
            
                if lunes <= cantidad_semanal.lunes and x.lunes:
                    obj.lunes = True
                if martes <= cantidad_semanal.martes and x.martes:
                    obj.martes = True
                if miercoles <= cantidad_semanal.miercoles and x.miercoles:
                    obj.miercoles = True
                if jueves <= cantidad_semanal.jueves and x.jueves:
                    obj.jueves = True
                if viernes <= cantidad_semanal.viernes and x.viernes:
                    obj.viernes = True
                obj.save()
                x.estado = 'SELECCIONADO'
                x.save()
                if(not obj.lunes and not obj.martes and not obj.miercoles and not obj.jueves and not obj.viernes):
                    obj.delete()
                    x.estado = 'PRESELECCION'
                    x.save()

                                
        print(options)
    context={'registro':registro,'lunes':lunes,'martes':martes,'miercoles':miercoles,'jueves':jueves,'viernes':viernes,'total':total,'cantidad_semanal':cantidad_semanal}
    return render(request, 'estudiantes_registrados.html', context)

def beneficiario(request):
    beneficiario = Beneficiario.objects.all()
    context={'beneficiario':beneficiario}
    return render(request, 'beneficiario.html', context)

def fallas(request):
    falla= Falla.objects.all()
    context={'falla':falla}
    return render(request, 'falla.html', context)   