from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import
from datetime import datetime, timedelta, time

@task(name="registra_falla")
def registro_falla(): 
    beneficiario = Beneficiario.objects.all()
    asitencia = Asistencia.objects.filter(fecha=datetime.datetime.today())
