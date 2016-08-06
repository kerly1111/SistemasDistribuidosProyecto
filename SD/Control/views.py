from django.shortcuts import render_to_response, RequestContext, redirect, HttpResponse,render
from django.contrib.auth import authenticate, login, logout
from Control.models import *
from .forms import *

from django.views.generic import FormView, ListView
import json
from django.core import serializers
import time
from datetime import datetime
import base64
from django.db import transaction


def index_view(request):
    return render_to_response('inicio.html',context=RequestContext(request))


#def login_view(request):
#   return  render_to_response('login.html',context=RequestContext(request))





def control(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                motes = Dispositivo(dis_nombre=request.POST['nombre'],
                             dis_mac=request.POST['mac'], dis_estado=request.POST['estado'], )

                motes.save()

                idmote = Dispositivo.objects.get(dis_nombre=request.POST["nombre"])

                sensor = Sensor(sen_nombre=request.POST['nombresensor'],
                                sen_unidadmedida=request.POST['unidadmedida'],
                                sen_localizacion=request.POST['localizacion'],
                                sen_estado=request.POST['estadosensor'],
                                dis_id=idmote, )

                sensor.save()

                idsensor = Sensor.objects.get(sen_nombre=request.POST["nombresensor"])

                actuador = Actuador(act_nombre=request.POST['nombreactuador'],
                                act_localizacion=request.POST['localizacionactuador'],
                                act_estado=request.POST['estadoactuador'],
                                sen_id=idsensor, )

                actuador.save()

                return redirect('inicio')
        except:
            return render_to_response('ingresardispositivos.html', context=RequestContext(request))

    return render_to_response('control.html', context=RequestContext(request))


def iot(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                motes = Dispositivo(dis_nombre=request.POST['nombre'],
                             dis_mac=request.POST['mac'], dis_estado=request.POST['estado'], )

                motes.save()

                idmote = Dispositivo.objects.get(dis_nombre=request.POST["nombre"])

                sensor = Sensor(sen_nombre=request.POST['nombresensor'],
                                sen_unidadmedida=request.POST['unidadmedida'],
                                sen_localizacion=request.POST['localizacion'],
                                sen_estado=request.POST['estadosensor'],
                                dis_id=idmote, )

                sensor.save()

                idsensor = Sensor.objects.get(sen_nombre=request.POST["nombresensor"])

                actuador = Actuador(act_nombre=request.POST['nombreactuador'],
                                act_localizacion=request.POST['localizacionactuador'],
                                act_estado=request.POST['estadoactuador'],
                                sen_id=idsensor, )

                actuador.save()

                return redirect('inicio')
        except:
            return render_to_response('iot.html', context=RequestContext(request))
    dis = Dispositivo.objects.all()
    act = Actuador.objects.all()
    sen = Sensor.objects.all()
    return render_to_response('iot.html',{'dis':dis,'sen':sen,'act':act}, context_instance=RequestContext(request))




def usuarios(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                motes = Dispositivo(dis_nombre=request.POST['nombre'],
                             dis_mac=request.POST['mac'], dis_estado=request.POST['estado'], )

                motes.save()

                idmote = Dispositivo.objects.get(dis_nombre=request.POST["nombre"])

                sensor = Sensor(sen_nombre=request.POST['nombresensor'],
                                sen_unidadmedida=request.POST['unidadmedida'],
                                sen_localizacion=request.POST['localizacion'],
                                sen_estado=request.POST['estadosensor'],
                                dis_id=idmote, )

                sensor.save()

                idsensor = Sensor.objects.get(sen_nombre=request.POST["nombresensor"])

                actuador = Actuador(act_nombre=request.POST['nombreactuador'],
                                act_localizacion=request.POST['localizacionactuador'],
                                act_estado=request.POST['estadoactuador'],
                                sen_id=idsensor, )

                actuador.save()

                return redirect('inicio')
        except:
            return render_to_response('usuarios.html', context=RequestContext(request))

    return render_to_response('usuarios.html', context=RequestContext(request))

def ingresardispositivos(request):
    if request.method == 'POST':

        try:
            with transaction.atomic():
                motes = Dispositivo(dis_nombre=request.GET['dis_nombre'],
                             dis_mac=request.GET['dis_mac'], dis_estado=request.GET['dis_estado'], )

                motes.save()

                serializado = json.dumps(["Ha guardado correctamente los datos", "success"])
                return HttpResponse(serializado, mimetype='application/json')
        except:
            return render_to_response('ingresardispositivos.html', context=RequestContext(request))






    return render_to_response('ingresardispositivos.html', context=RequestContext(request))


def editardispositivos(request,id):
    if request.method == 'POST':

        try:
            with transaction.atomic():
                motes = Dispositivo(dis_id=id,dis_nombre=request.POST['dis_nombre'],
                             dis_mac=request.POST['dis_mac'], dis_estado=request.POST['dis_estado'], )

                motes.save()

                return redirect('iot')
        except:
            return render_to_response('editardispositivos.html', context=RequestContext(request))

    dis = Dispositivo.objects.get(pk=id)
    return render_to_response('editardispositivos.html',{'dis':dis}, context_instance=RequestContext(request))


def ingresaractuadores(request):
    if request.method == 'POST':

        try:
            with transaction.atomic():

                dis = Dispositivo.objects.get(pk=request.POST["dis_id"])
                act = Actuador(act_nombre=request.POST['act_nombre'],
                             act_localizacion=request.POST['act_localizacion'], act_funcion=request.POST['act_funcion'],
                             act_estado = request.POST['act_estado'],
                             dis_id=dis)

                act.save()



                return redirect('iot')
        except:
            return render_to_response('ingresaractuadores.html', context=RequestContext(request))

    dis = Dispositivo.objects.all()
    return render_to_response('ingresaractuadores.html',{'dis':dis}, context_instance=RequestContext(request))


def editaractuadores(request,id):
    if request.method == 'POST':

        try:
            with transaction.atomic():
                dis = Dispositivo.objects.get(pk=request.POST["dis_id"])
                act = Actuador(act_id=id,act_nombre=request.POST['act_nombre'],
                             act_localizacion=request.POST['act_localizacion'], act_funcion=request.POST['act_funcion'],
                             act_estado=request.POST['act_estado'],
                             dis_id=dis,)

                act.save()

                return redirect('iot')
        except:
            return render_to_response('editaractuadores.html', context=RequestContext(request))

    act = Actuador.objects.get(pk=id)
    dis = Dispositivo.objects.all()
    return render_to_response('editaractuadores.html',{'act':act,'dis':dis}, context_instance=RequestContext(request))

def ingresarsensores(request):
    if request.method == 'POST':

        try:
            with transaction.atomic():
                dis = Dispositivo.objects.get(pk=request.POST["dis_id"])
                sen = Sensor(sen_nombre=request.POST['sen_nombre'],
                             sen_unidadmedida=request.POST['sen_unidadmedida'],
                             sen_localizacion=request.POST['sen_localizacion'], sen_estado=request.POST['sen_estado'],
                             sen_tipo = request.POST['sen_tipo'],
                             dis_id=dis,)

                sen.save()



                return redirect('iot')
        except:
            return render_to_response('ingresarsensores.html', context=RequestContext(request))

    dis = Dispositivo.objects.all()
    return render_to_response('ingresarsensores.html',{'dis':dis}, context_instance=RequestContext(request))

def sensores(request):

    sen = Sensor.objects.filter(dis_id_id = request.GET["codigo"])
    return render_to_response('sensores.html',{'sen':sen}, context_instance=RequestContext(request))


def buscardispositivos(request):

    dis = Dispositivo.objects.filter(dis_nombre__contains = request.GET["buscar"])
    return render_to_response('buscardispositivos.html',{'dis':dis}, context_instance=RequestContext(request))

def buscaractuadores(request):

    act = Actuador.objects.filter(act_nombre__contains = request.GET["buscar"])
    return render_to_response('buscaractuadores.html',{'act':act}, context_instance=RequestContext(request))

def buscarsensores(request):

    sen = Sensor.objects.filter(sen_nombre__contains = request.GET["buscar"])
    return render_to_response('buscarsensores.html',{'sen':sen}, context_instance=RequestContext(request))


def editarsensores(request,id):
    if request.method == 'POST':

        try:
            with transaction.atomic():
                dis = Dispositivo.objects.get(pk=request.POST["dis_id"])
                sen = Sensor(sen_id=id,sen_nombre=request.POST['sen_nombre'],
                             sen_unidadmedida=request.POST['sen_unidadmedida'],
                             sen_localizacion=request.POST['sen_localizacion'], sen_estado=request.POST['sen_estado'],
                             sen_tipo = request.POST['sen_tipo'],
                             dis_id=dis,)
                sen.save()

                return redirect('iot')
        except:
            return render_to_response('editarsensores.html', context=RequestContext(request))

    dis = Dispositivo.objects.all()
    sen = Sensor.objects.get(pk=id)
    return render_to_response('editarsensores.html',{'sen':sen,'dis':dis}, context_instance=RequestContext(request))