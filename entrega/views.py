from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
<<<<<<< HEAD
=======
    
>>>>>>> c4972948245d3e0bebd994fddb92ac8b910f1519
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

def entrega(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'entrega.html', context)

def perfil(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'perfil.html', context)

def configuracion(request):
   # entregado = Entrega.objects.all()
    context={}
    return render(request, 'configuracion.html', context)