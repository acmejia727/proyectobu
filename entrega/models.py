from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#<<<<<<< HEAD
    
#=======
TIPO_BENEFICIO = [
    ('REFRIGERIO', 'REFRIGERIO'),
    ('ALMUERZO', 'ALMUERZO'),
]

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    foto = models.ImageField(upload_to="perfil/", null=True)
    fecha_creacion = models.DateField(auto_now=True)
    
    class Meta:
         verbose_name_plural = "Personal"

#<<<<<<< HEAD
    def __str__(self):
        return self.user
#=======
    class Meta:
         verbose_name_plural = "Personal"

    def __str__(self):
        return str(self.user)
#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24

class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    carrera = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="perfil/", null=True)
    fecha_creacion = models.DateField(auto_now=True)
    
    class Meta:
         verbose_name_plural = "Estudiante"

#<<<<<<< HEAD
    def __str__(self):
        return self.user
#=======
    class Meta:
         verbose_name_plural = "Estudiante"

    def __str__(self):
        return str(self.user)
#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24

class Tipo_beneficio(models.Model):
    nombre = models.CharField(max_length=50, null=False,choices=TIPO_BENEFICIO)
    descripcion = models.CharField(max_length=200, null=True)
      
    class Meta:
         verbose_name_plural = "Tipo de beneficio"

#<<<<<<< HEAD
#=======
    class Meta:
         verbose_name_plural = "Tipo de beneficio"

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    def __str__(self):
        return str(self.nombre)

class Convocatoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateField(auto_now=True)
      
    class Meta:
         verbose_name_plural = "Convocatoria"

#<<<<<<< HEAD
#=======
    class Meta:
         verbose_name_plural = "Convocatoria"

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    def __str__(self):
        return str(self.nombre)

class Beneficiario(models.Model):
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE, verbose_name="Convocatoria")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Convocatoria", null=True,blank=False)
    fecha_creacion = models.DateField(auto_now=True)
      
    class Meta:
         verbose_name_plural = "Beneficiario"

#<<<<<<< HEAD
#=======
    class Meta:
         verbose_name_plural = "Beneficiario"

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    def __str__(self):
        return "Beneficiario con tipo de beneficio: ", self.tipo_beneficio, " en la convocatoria: ", self.convocatoria

class Horario(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
      
    class Meta:
         verbose_name_plural = "Horario"

#<<<<<<< HEAD
#=======
    class Meta:
         verbose_name_plural = "Horario"

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    def __str__(self):
        return "Hora inicial: ", self.fecha_inicio, " hora final: ", self.fecha_final

class Modulo(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario")
    tipo_beneficio = models.ForeignKey(Tipo_beneficio, on_delete=models.CASCADE, verbose_name="Tipo beneficio")
      
    class Meta:
         verbose_name_plural = "Modulo"

#<<<<<<< HEAD
#=======
    class Meta:
         verbose_name_plural = "Modulo"

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    def __str__(self):
        return self.horario

class Asistencia(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name="Modulo")
    fecha = models.DateField(auto_now=True)
      
    class Meta:
         verbose_name_plural = "Asistencia"

    def __str__(self):
        return "Asistencia del beneficiario: ", self.beneficiario, " en el modulo: ", self.modulo

    class Meta:
         verbose_name_plural = "Asistencia"

    def __str__(self):
        return "Asistencia del beneficiario: ", self.beneficiario, " en el modulo: ", self.modulo

class Acceso_Modulo(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name="Personal")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, verbose_name="Modulo")
#<<<<<<< HEAD
      
#=======

#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
    class Meta:
         verbose_name_plural = "Acceso del modulo"

    def __str__(self):
        return "Acceso del modulo desde el personal: ", self.personal, " en el modulo: ", self.modulo

#<<<<<<< HEAD
    
#=======
#>>>>>>> 665afe2e9c565bede0ab20287c636d94ec438a24
