from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class PersonalAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('user','fecha_creacion')
    class Meta:
        model = Personal
# Register your models here.
admin.site.register(Personal, PersonalAdmin)

admin.site.register(Estudiante)
admin.site.register(Beneficiario)
admin.site.register(Tipo_beneficio)
admin.site.register(Convocatoria)

admin.site.register(Acceso_Modulo)
admin.site.register(Modulo)
admin.site.register(Horario)
admin.site.register(Cantidad_semanal)
admin.site.register(Asistencia)
admin.site.register(Registro_estudiante)

