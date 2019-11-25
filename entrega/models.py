from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TIPO_BENEFICIO = [
    ('REFRIGERIO', 'REFRIGERIO'),
    ('ALMUERZO', 'ALMUERZO'),
]

SELECCION = [
    ('SELECCION', 'SELECCION'),
    ('PRESELECCION', 'PRESELECCION'),
]

TIPO_PROVEEDOR = [
    ('CARNES', 'CARNES'),
    ('BEBIDAS', 'BEBIDAS'),
    ('LACTAEO', 'LACTEOS'),
    ('FRUTAS Y VERDURAS', 'FRUTAS Y VERDURAS'),
    ('GRANOS', 'GRANOS'),
    ('OTROS', 'OTROS'),
]

ESTADO = [
    ('SOLICITADO', 'SOLICITADO'),
    ('EN PROCESO', 'EN PROCESO'),
     ('ENTREGADO', 'ENTEGRADO'),
     ('RECHAZADO', 'RECHAZADO'),
]

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    encargado_sede = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)


class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    foto = models.ImageField(upload_to="perfil/", null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name_plural = "Personal"

    def __str__(self):
        return str(self.user)


class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    carrera = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="perfil/", null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    estrato = models.IntegerField(null=True)
    pension_ud = models.IntegerField(null=True)
    pension_de = models.IntegerField(null=True)
    jovenes_accion = models.BooleanField(null=True)
    deportista = models.BooleanField(null=True)

    class Meta:
         verbose_name_plural = "Estudiante"

    def __str__(self):
        return str(self.user)

class Registro_estudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante",null=True)
    estado = models.CharField(choices=SELECCION,max_length=100,default='PRESELECCION')
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    tipo_beneficio = models.CharField(choices=TIPO_BENEFICIO,max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="sede",null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)


class Cantidad_semanal(models.Model):
    lunes = models.IntegerField()
    martes = models.IntegerField()
    miercoles = models.IntegerField()
    jueves = models.IntegerField()
    viernes = models.IntegerField()


class Tipo_beneficio(models.Model):
    nombre = models.CharField(max_length=50, null=False,choices=TIPO_BENEFICIO)
    descripcion = models.CharField(max_length=200, null=True)
    cantidad = models.ForeignKey(Cantidad_semanal, on_delete=models.CASCADE, verbose_name="Cantidad",null=True)

    class Meta:
         verbose_name_plural = "Tipo de beneficio"

    def __str__(self):
        return str(self.nombre)


class Convocatoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name_plural = "Convocatoria"

    def __str__(self):
        return str(self.nombre)

class Beneficiario(models.Model):
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE, verbose_name="Convocatoria")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Convocatoria", null=True,blank=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="sede",null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name_plural = "Beneficiario"

    def __str__(self):
        return "Beneficiario con tipo de beneficio: "+ str(self.tipo_beneficio) +" en la convocatoria: "+ str(self.convocatoria)

class Horario(models.Model):
    fecha_ini = models.TimeField(null=True)
    fecha_fin = models.TimeField(null=True)

    class Meta:
         verbose_name_plural = "Horario"

    def __str__(self):
        return "Hora inicial: "+ str(self.fecha_ini)+ " hora final: "+str(self.fecha_fin)

class Modulo(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario")
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")

    class Meta:
         verbose_name_plural = "Modulo"

    def __str__(self):
        return str(self.horario)


class Acceso_Modulo(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name="Personal")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name="Modulo")

    class Meta:
         verbose_name_plural = "Acceso del modulo"

    def __str__(self):
        return "Acceso del modulo desde el personal: "+ str(self.personal)+" en el modulo: "+str(self.modulo)

class Asistencia(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    acceso_modulo = models.ForeignKey(Acceso_Modulo, on_delete=models.CASCADE, verbose_name="Acceso Modulo",null=True)
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name_plural = "Asistencia"

    def __str__(self):
        return "Asistencia del beneficiario: "+str(self.beneficiario)+" en el modulo: "+str(self.acceso_modulo)

class Falla(models.Model):
    cantidad = models.IntegerField()
    sanciones = models.IntegerField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante",null=True)
    estado = models.CharField(max_length=100)

class Registro_falla(models.Model):
    falla =  models.ForeignKey(Falla, on_delete=models.CASCADE, verbose_name="Falla",null=True)  
    fecha = models.DateTimeField(auto_now=True)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    suministro =  models.CharField(max_length=100)
    tipo =  models.CharField(max_length=100,choices=TIPO_PROVEEDOR)

    def __str__(self):
        return str(self.nombre)+" - "+str(self.tipo)

    
class Registro_pedido(models.Model):
    pedido = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=100,choices=ESTADO)
    comentario = models.CharField(max_length=200)
    proveedor =  models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor",null=True)  
    fecha = models.DateTimeField(auto_now=True)



