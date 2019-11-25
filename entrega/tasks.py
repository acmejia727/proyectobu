from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from celery import shared_task
from .models import *
#from datetime import datetime, timedelta, time
from datetime import date,timedelta, time
@shared_task(name="registra_falla")
def registro_falla(name, *args, **kwargs):

    beneficiario = Beneficiario.objects.all()
    #crear fallas
    for x in beneficiario:

        #si el estudinate no reclama beneficio se marca como incumplido
        asistencia = Asistencia.objects.filter(fecha__date=date.today(),beneficiario_id=x.id)
        if asistencia:
            print('no tiene falla '+str(x.id))            
        else:
            try:
                falla = Falla.objects.get(estudiante_id=x.estudiante.id)
                if falla.sanciones <= 5:
                    falla.cantidad = falla.cantidad + 1                
                    falla.save()                
            except:
                falla = Falla.objects.create(cantidad=1,sanciones=0,estudiante=Estudiante.objects.get(id=x.estudiante.id),estado='activo')
            
            reg_falla =  Registro_falla.objects.create(falla=Falla.objects.get(id=falla.id))
    

        try:
            falla_data = Falla.objects.get(estudiante=x.estudiante.id)
        except:
            falla_data = False
        if falla_data:


            count = 0   
            if x.lunes:
                count = count+1
            if x.martes:
                count = count+1
            if x.miercoles:
                count = count+1
            if x.jueves:
                count = count+1
            if x.viernes:
                count = count+1
            
            one_week_ago = date.today() - timedelta(days=7)
            registro = Registro_falla.objects.filter(fecha__gte=one_week_ago,falla__estudiante_id=x.estudiante.id)
        #si el usaurio no reclama de maera consecutiva durante una semana se saciona por un mes
            print(count,registro.count())
            if registro.count() > count:
                falla_data.estado = '30 dias'
                if falla_data.sanciones < 5:
                    falla_data.sanciones = falla_data.sanciones+1
                    falla_data.save()

             #dos saciones maxima
            print('maximo'+str(falla_data.sanciones))
            if(falla_data.sanciones > 2):
                falla_data.estado = 'Indefinidad'
                falla_data.save()

            #levantar sancion
            if falla_data.estado == '30 dias':
                mes = date.today() - timedelta(days=7)
                registro = Registro_falla.objects.filter(fecha__gte=mes,falla__estudiante_id=x.estudiante.id)
                if registro.count() < 1:
                    falla_data.estado = 'activo'
                    falla_data.save()
                    

        
        




