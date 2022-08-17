from django import views
from django.contrib import admin
from django.urls import path
from modulo_expediente.views.Expediente import (antecedentesUpdate, busqueda_paciente, 
    autocompletado_apellidos, eliminar_cola, sala_consulta,get_cola,get_paciente,agregar_cola, 
    modificar_signosVitales, crear_expediente, editar_consulta, 
    CreateControlSubsecuente, buscar_expediente, 
    AgendaView, ConsultaView, ExamenesExternosCreateView, storageurl)
    
from modulo_expediente.views.EvolucionConsulta import (DeleteNotaEvolucion,ListaHojaEvolucion,CreateHojaEvolucion,UpdateNotaEvolucion)
from modulo_expediente.views.ConstanciaMedica import (ConstanciaMedicaPDFView,ConstanciaMedicaCreate, ConstanciaMedicaView, ConstanciaMedicaUpdate)
from modulo_expediente.views.Medicamento import (dosis_medicamento, eliminar_dosis,
agregar_medicamento, busqueda_medicamento, autocompletado_medicamento)
from modulo_expediente.views.ReferenciaMedica import (ReferenciaMedicaView,
ReferenciaMedicaUpdate, ReferenciaMedicaPdfView)
from modulo_expediente.views.RecetaMedica import RecetaMedicaPdfView
urlpatterns = [
    # Expediente
    path('paciente/',busqueda_paciente, name='busqueda_paciente'),
    path('buscar/',buscar_expediente,name='buscar_expediente'),
    path('paciente/<int:id_paciente>',get_paciente, name='get_paciente'),
    path('paciente/datos',crear_expediente,name='crear_expediente'),
    path('paciente/autocompletado',autocompletado_apellidos, name='autocompletado_apellidos'),
    # SALA
    path('sala/',sala_consulta, name='sala_consulta'),
    path('cola/<int:id_paciente>', agregar_cola,name='agregar_cola' ),
    path('cola/', get_cola, name='get_contieneConsulta'),
    path('cola/eliminar-paciente/<int:id_paciente>', eliminar_cola, name='eliminar_cola'),
    # Signos Vitales
    path('modificar-signosVitales/<int:id_consulta>',modificar_signosVitales, name='modificar_signosVitales'),
    # Antecedentes
    path('consulta/<int:id_expediente>/antecedentes-personales/',antecedentesUpdate,name='antecedentes-update'),
    path('consulta/<int:id_consulta>/receta-medica/pdf',RecetaMedicaPdfView.as_view(),name='receta-medica-pdf' ),
    # Constancias Medicas
    path('consulta/<int:id_consulta>/constancia-medica/pdf', ConstanciaMedicaPDFView.as_view(),name='constancia-medica'),
    path('consulta/<int:id_consulta>/constancia-medica/<int:id_constancia>/',ConstanciaMedicaUpdate.as_view(),name='constancia-medica-update'),
    path('constancia-medica/<str:id>',ConstanciaMedicaView.as_view(),name='constancia-medica'),
    path('constancia-medica/',ConstanciaMedicaCreate.as_view(),name='crear-constancia-medica'),
    # Referencias Medicas
    path('consulta/<int:id_consulta>/referencia-medica/',ReferenciaMedicaView.as_view(),name='referencia-medica'),
    path('consulta/<int:id_consulta>/referencia-medica/pdf/<int:id_referencia_medica>/',ReferenciaMedicaPdfView.as_view(),name='referencia-medica-pdf' ),
    path('consulta/<int:id_consulta>/referencia-medica/<int:id_referencia>/',ReferenciaMedicaUpdate.as_view(),name='referencia-medica-update'),
    # Medicamentos
    path('receta_medica/agregar-medicamento', agregar_medicamento, name='agregar_nuevo_medicamento'),
    path('receta/dosis',dosis_medicamento,name='agregar_dosis'),
    path('receta/dosis/eliminar_dosis/<int:id_dosis>',eliminar_dosis,name='eliminar_dosis'),
    path('consulta/<int:id_consulta>/',ConsultaView.as_view(),name='editar_consulta'),
    path('medicamento/',busqueda_medicamento, name='agregar_medicamento'),
    path('medicamento/autocompletado/',autocompletado_medicamento, name='agregar_medicamento_2'),
    # Evolucion Consulta
    path('consulta/<int:id_consulta>/hoja-evolucion/',CreateHojaEvolucion.as_view(),name='hoja-evolucion-create'),
    path('consulta/<int:id_consulta>/hoja-evolucion/<int:id_nota_evolucion>',DeleteNotaEvolucion.as_view(),name='hoja-evolucion-delete'),
    path('consulta/<int:id_consulta>/hoja-evolucion/update',UpdateNotaEvolucion.as_view(),name='hoja-evolucion-update'),
    path('consulta/<int:id_consulta>/hoja-evolucion/lista',ListaHojaEvolucion.as_view(),name='hoja-evolucion-lista'),
    # Control Subsecuente
    path('consulta/<int:id_consulta>/control-subsecuente/',CreateControlSubsecuente.as_view(),name='control-subsecuente-create'),
    # Agenda
    path('agenda/', AgendaView.as_view(),name='ver_agenda'),
    ###URL de Pruebas para visualización de archivos en S3
   # path('documento/<int:id_documento>/', storageurl, name="storage-url")
    path('consulta/<int:id_consulta>/agregar-documento-externo/', ExamenesExternosCreateView.as_view(), name="create_examenes_externos"),
    path('documento/<int:id_documento>/', storageurl, name="storage-url")
    
]

