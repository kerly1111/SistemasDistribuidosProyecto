from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.




class Dispositivo(models.Model):
    dis_id = models.AutoField(primary_key=True)
    dis_nombre=models.CharField(max_length=20,null=False)
    dis_mac=models.CharField(max_length=100,null=False)
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )
    dis_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')

    def __str__(self):
        return self.dis_nombre


class Actuador(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_nombre=models.CharField(max_length=20)
    act_localizacion=models.CharField(max_length=100)

    FUN_CHOICES = (
        (u'e', u'Encendido'),
        (u'a', u'Apagado'),
    )

    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )

    act_funcion = models.CharField(max_length=1, choices=FUN_CHOICES, default='a')
    act_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')
    dis_id = models.ForeignKey(Dispositivo)

    def __str__(self):
        return self.act_nombre

class Sensor(models.Model):
    sen_id = models.AutoField(primary_key=True)
    sen_nombre=models.CharField(max_length=20)
    sen_unidadmedida=models.CharField(max_length=100)
    sen_localizacion=models.CharField(max_length=100)
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )

    TIP_CHOICES = (
        (u'a', u'Activador'),
        (u'i', u'Informativo'),
    )
    sen_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')
    sen_tipo = models.CharField(max_length=1, choices=TIP_CHOICES, default='a')
    dis_id = models.ForeignKey(Dispositivo)

    def __str__(self):
        return self.sen_nombre

class Regla(models.Model):
    sen_id=models.ForeignKey(Sensor)
    act_id=models.ForeignKey(Actuador)


class Empresa(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_nombre=models.CharField(max_length=60)
    emp_decripcion=models.CharField(max_length=100)
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )
    emp_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')


    def __str__(self):
        return self.emp_nombre



class UsuarioDispositivo(models.Model):
    username=models.ForeignKey(User)
    dis_id=models.ForeignKey(Dispositivo)


class Registro(models.Model):
    reg_id=models.AutoField(primary_key=True)
    reg_fecha_hora=models.CharField(max_length=60)
    reg_hora=models.CharField(max_length=20)
    reg_fecha=models.CharField(max_length=20)
    username=models.ForeignKey(User)
    sen_id = models.ForeignKey(Sensor)

def __str__(self):
    return self.fecha_hora_registro
