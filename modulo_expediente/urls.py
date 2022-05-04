from django import views
from django.contrib import admin
from django.urls import path
from modulo_expediente.views import busqueda_paciente , get_paciente, vista_sala_espera


urlpatterns = [
    path('paciente/',busqueda_paciente, name='busqueda_paciente'),
    path('paciente/<int:id_paciente>',get_paciente, name='get_paciente'),
    path('sala/', vista_sala_espera, name='salaEspera')
]