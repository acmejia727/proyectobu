# Generated by Django 2.2.4 on 2019-09-14 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0005_auto_20190908_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acceso_modulo',
            options={'verbose_name_plural': 'Acceso del modulo'},
        ),
        migrations.AlterModelOptions(
            name='asistencia',
            options={'verbose_name_plural': 'Asistencia'},
        ),
        migrations.AlterModelOptions(
            name='beneficiario',
            options={'verbose_name_plural': 'Beneficiario'},
        ),
        migrations.AlterModelOptions(
            name='convocatoria',
            options={'verbose_name_plural': 'Convocatoria'},
        ),
        migrations.AlterModelOptions(
            name='estudiante',
            options={'verbose_name_plural': 'Estudiante'},
        ),
        migrations.AlterModelOptions(
            name='horario',
            options={'verbose_name_plural': 'Horario'},
        ),
        migrations.AlterModelOptions(
            name='modulo',
            options={'verbose_name_plural': 'Modulo'},
        ),
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name_plural': 'Personal'},
        ),
        migrations.AlterModelOptions(
            name='tipo_beneficio',
            options={'verbose_name_plural': 'Tipo de beneficio'},
        ),
    ]
