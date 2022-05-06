from time import time
from django.shortcuts import render
from modulo_expediente.serializers import PacienteSerializer, ContieneConsultaSerializer
from django.core import serializers
from datetime import datetime
from modulo_expediente.filters import PacienteFilter
from modulo_expediente.models import Consulta, Paciente, ContieneConsulta, Expediente
from django.http import JsonResponse
import json
from datetime import date
# Create your views here.

def busqueda_paciente(request):
    result= PacienteFilter(request.GET, queryset=Paciente.objects.all())
    pacientes =PacienteSerializer(result.qs, many=True)
    return JsonResponse({'data':pacientes.data})
     #la clave tiene que ser data para que funcione con el metodo. 

def autocompletado_apellidos(request):
    
    apellidos=Paciente.objects.values("apellido_paciente").all()
    apellidosList=[]
    for apellido in apellidos:
        apellidosList.append(apellido['apellido_paciente'])
    return JsonResponse({"data":apellidosList})
    #la clave tiene que ser data para que funcione con el metodo. 

def sala_consulta(request):
    return render(request,"expediente/sala.html")

#Metodo que devuelve los datos del paciente en json
def get_paciente(request, id_paciente):
    paciente=Paciente.objects.filter(id_paciente=id_paciente)
    serializer=PacienteSerializer(paciente, many= True)
    return JsonResponse(serializer.data, safe=False)

#Metodo que devuelve los datos del objeto contiene consulta en json
def agregar_cola(request, id_paciente):
    expediente=Expediente.objects.get(id_paciente_id=id_paciente)
    codExpediente=expediente.id_expediente
    fecha=datetime.now()
    try:
        numero=ContieneConsulta.objects.filter(fecha_de_cola__year=fecha.year, 
                         fecha_de_cola__month=fecha.month, 
                         fecha_de_cola__day=fecha.day).last().numero_cola +1
    except:
        numero=1
    #Creando Objeto contieneCola
    try:
        contieneconsulta=ContieneConsulta()
        contieneconsulta.expediente=expediente
        contieneconsulta.numero_cola=numero
        contieneconsulta.consumo_medico=0
        contieneconsulta.estado_cola_medica='1'
        contieneconsulta.fase_cola_medica='2'
        contieneconsulta.save()
        response={
            'type':'sucess'
        }
    except:
        response={
            'type':'error'
        }
    
    return JsonResponse(response, safe=False)

#Metodo que devuelve una lista de constieneConsulta filtrado por la fecha de hoy
def  get_contieneConsulta(request):
    fecha=datetime.now()
    '''
    contiene_consulta=list(ContieneConsulta.objects.values())
    lista=[]
    for i in range(len(contiene_consulta)):
        if contiene_consulta[i]["fecha_de_cola"] == fecha_actual:
            diccionario={
                "id":"",
                "numero_cola":"",
                "fecha_de_cola":"",
                "consumo_medico":"",
                "estado_cola_medica":"",
                "fase_cola_medica":"",
                "consulta_id":"",
                "expediente_id":""
            }
            diccionario["id"]= contiene_consulta[i]["id"]
            diccionario["numero_cola"]= contiene_consulta[i]["numero_cola"]
            diccionario["fecha_de_cola"]= contiene_consulta[i]["fecha_de_cola"]
            diccionario["consumo_medico"]= contiene_consulta[i]["consumo_medico"]
            diccionario["estado_cola_medica"]= contiene_consulta[i]["estado_cola_medica"]
            diccionario["fase_cola_medica"]= contiene_consulta[i]["fase_cola_medica"]
            diccionario["consulta_id"]= contiene_consulta[i]["consulta_id"]
            diccionario["expediente_id"]= contiene_consulta[i]["expediente_id"]
            lista.append(diccionario)
            del diccionario
            '''
    contieneconsulta=ContieneConsulta.objects.filter(fecha_de_cola__year=fecha.year, 
                    fecha_de_cola__month=fecha.month, 
                    fecha_de_cola__day=fecha.day)
    serializer=ContieneConsultaSerializer(contieneconsulta, many=True)
    return JsonResponse(serializer.data, safe=False)
