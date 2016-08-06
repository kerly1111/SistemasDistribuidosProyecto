from django.shortcuts import render
from Control.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer
    queryset = Dispositivo.objects.all()

class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

class ActuadorViewSet(viewsets.ModelViewSet):
    serializer_class = ActuadorSerializer
    queryset = Actuador.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewLogin(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = User.object.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        msj = 'ingresa post'
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            username = str(serializer.data['username'])
            password = str(serializer.data['password'])
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    datos = {'status':'Login Satisfactorio',
                             'usu_nombre': user.usu_nombre,
                             'usu_apellido': user.usu_apellido,
                             'username':user.username,
                             'usu_correo':user.usu_correo}
                else:
                    datos = {'status': 'Cuenta Deshabilitada',
                             'usu_nombre': '',
                             'usu_apellido': '',
                             'username':'',
                             'usu_correo':''}
            else:
                datos = {'status':'Loggin invalido',
                         'usu_nombre': '',
                         'usu_apellido': '',
                         'username':'',
                         'usu_correo':''}

            print(datos)
            return Response(datos)
        else:
            return Response({'status': msj})