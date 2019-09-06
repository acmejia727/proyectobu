# Generated by Django 2.2.4 on 2019-09-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0002_auto_20190906_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_reg', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='beneficiario',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='modulo',
        ),
        migrations.RemoveField(
            model_name='beneficiario',
            name='convocatoria',
        ),
        migrations.RemoveField(
            model_name='beneficiario',
            name='tipo_beneficio',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='user',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='tipo_beneficio',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Acceso_Modulo',
        ),
        migrations.DeleteModel(
            name='Asistencia',
        ),
        migrations.DeleteModel(
            name='Beneficiario',
        ),
        migrations.DeleteModel(
            name='Convocatoria',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.DeleteModel(
            name='Modulo',
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
        migrations.DeleteModel(
            name='Tipo_beneficio',
        ),
    ]