from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    entregado = Entrega.objects.all()
    context={'entregado':entregado}
    return render(request, 'index.html', context)

def registro(request):
    
    context={}
    return render(request, 'registro.html', context)