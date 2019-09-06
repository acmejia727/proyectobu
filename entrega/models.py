from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    foto = models.ImageField(upload_to="perfil/", null=True)
    fecha_creacion = models.DateField(auto_now=True)


class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    carrera = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()
    foto = models.CharField(max_length=300, null=True)
    fecha_creacion = models.DateField(auto_now=True)


class Tipo_beneficio(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True)


class Convocatoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateField(auto_now=True)


class Beneficiario(models.Model):
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE, verbose_name="Convocatoria")
    fecha_creacion = models.DateField(auto_now=True)


class Horario(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()


class Modulo(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario")
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")


class Asistencia(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name="Modulo")
    fecha = models.DateField(auto_now=True)


class Acceso_Modulo(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name="Personal")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name="Modulo")
