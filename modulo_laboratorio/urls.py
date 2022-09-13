from django.urls import path
from modulo_laboratorio.views.CategoriaExamen import *
from modulo_laboratorio.views.EsperaExamen import *
from modulo_laboratorio.views.Resultado import *
from modulo_laboratorio.views.OrdenExamenes import *

urlpatterns = [
    path('sala/', sala_laboratorio, name='sala_laboratorio'),

    path('examen/', agregar_examen_cola, name='agregar_examen_cola' ),

    path('examen/<int:id_categoria>', get_categoria_examen, name='get_select_examen' ),

    # path('examen/cola/', get_cola_examenes, name='get_cola_examenes'),
    # path('examen/resultado/<int:id_resultado>', elaborar_resultados_examen, name='elaborar_resultado'),

    path('examen/resultado/<int:orden_id>/pdf', generar_pdf, name='generar_pdf'),
    path('examen/cola/fase/2',cambiar_fase_secretaria,name="cambiar_fase_secretaria"),#cambia a fase en proceso
    # path('examen/cola/fase/3',cambiar_fase_laboratorio,name="cambiar_fase_laboratorio"),#cambia a fase en proceso

    path('inicio/', inicio, name='inicio_lab'),
    # path('pendientes/', examenes_pendientes, name='pendientes_lab'),
    # path('bitacora/', bitacora_templete, name='bitacora_lab'),

    path('orden/<int:id_paciente>', OrdenExamenCreate.as_view(),name="crear_orden_examenes"),
    path('orden/<int:id_paciente>/<int:id_orden>', OrdenExamenUpdate.as_view(),name="update_orden_examenes")

]
