from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from entrega.models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

# Create your views here.
@login_required(login_url='/')
def perfilEstudiante(request):
    try:
        falla = Falla.objects.get(estudiante__user__id=request.user.id)
    except:
        falla = False

    try:
        registro = Registro_estudiante.objects.get(estudiante__user__id=request.user.id)    
    except:
        registro = False
    try:
        perfil = Estudiante.objects.get(user__id=request.user.id)
    except:
        perfil = False
    reg_falla =  Registro_falla.objects.filter(falla__estudiante__user__id=request.user.id)[:5]
    beneficio = Beneficiario.objects.filter(estudiante__user__id=request.user.id)
    asistencia = Asistencia.objects.filter(beneficiario__estudiante__user__id=request.user.id).order_by('-fecha')[:10]
    # entregado = Entrega.objects.all()
    context={'perfil':perfil,'beneficio':beneficio,'registro':registro,'asistencia':asistencia,'reg_falla':reg_falla,'falla':falla}
    return render(request, 'perfil_estudiante.html', context)

@login_required(login_url='/')
def inscripcion(request):
    print(request.user.id)   
    if request.method == 'POST':
       
       form = FormInscripcion(request.POST, request.FILES)    
       formestudent = form.save(commit=False)
       formestudent.estudiante = Estudiante.objects.get(user__id=request.user.id)
       form.save()      
       
       return HttpResponseRedirect('/perfilEstudiante/')
    else:
        form = FormInscripcion()
  
    
    context={'perfil':"perfil",'form':form}
    return render(request, 'inscripcion.html', context)    


