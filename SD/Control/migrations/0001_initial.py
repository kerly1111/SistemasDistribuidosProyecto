# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuador',
            fields=[
                ('act_id', models.AutoField(serialize=False, primary_key=True)),
                ('act_nombre', models.CharField(max_length=20)),
                ('act_localizacion', models.CharField(max_length=100)),
                ('act_funcion', models.CharField(default='a', max_length=1, choices=[('e', 'Encendido'), ('a', 'Apagado')])),
                ('act_estado', models.CharField(default='a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('dis_id', models.AutoField(serialize=False, primary_key=True)),
                ('dis_nombre', models.CharField(max_length=20)),
                ('dis_mac', models.CharField(max_length=100)),
                ('dis_estado', models.CharField(default='a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('emp_id', models.AutoField(serialize=False, primary_key=True)),
                ('emp_nombre', models.CharField(max_length=60)),
                ('emp_decripcion', models.CharField(max_length=100)),
                ('emp_estado', models.CharField(default='a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('reg_id', models.AutoField(serialize=False, primary_key=True)),
                ('reg_fecha_hora', models.CharField(max_length=60)),
                ('reg_hora', models.CharField(max_length=20)),
                ('reg_fecha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Regla',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('act_id', models.ForeignKey(to='Control.Actuador')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sen_id', models.AutoField(serialize=False, primary_key=True)),
                ('sen_nombre', models.CharField(max_length=20)),
                ('sen_unidadmedida', models.CharField(max_length=100)),
                ('sen_localizacion', models.CharField(max_length=100)),
                ('sen_estado', models.CharField(default='a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
                ('sen_tipo', models.CharField(default='a', max_length=1, choices=[('a', 'Activador'), ('i', 'Informativo')])),
                ('dis_id', models.ForeignKey(to='Control.Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioDispositivo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dis_id', models.ForeignKey(to='Control.Dispositivo')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='regla',
            name='sen_id',
            field=models.ForeignKey(to='Control.Sensor'),
        ),
        migrations.AddField(
            model_name='registro',
            name='sen_id',
            field=models.ForeignKey(to='Control.Sensor'),
        ),
        migrations.AddField(
            model_name='registro',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actuador',
            name='dis_id',
            field=models.ForeignKey(to='Control.Dispositivo'),
        ),
    ]
