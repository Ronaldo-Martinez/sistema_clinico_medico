from django.urls import path
from modulo_expediente.views.Expediente import ( busqueda_paciente, 
    autocompletado_apellidos, sala_consulta,get_paciente, crear_expediente, buscar_expediente, RegistroMasivoExpedientesView)
from modulo_expediente.views.ConsultaMedica import (ConsultaView,antecedentesUpdateView)    
from modulo_expediente.views.SignosVitales import (crear_signos_vitales, modificar_signosVitales,get_signos_vitales)    

from modulo_expediente.views.EvolucionConsulta import (DeleteNotaEvolucion,ListaHojaEvolucion,CreateHojaEvolucion,UpdateNotaEvolucion)
from modulo_expediente.views.ConstanciaMedica import (ConstanciaMedicaPDFView,ConstanciaMedicaCreate, ConstanciaMedicaView, ConstanciaMedicaUpdate)
from modulo_expediente.views.Medicamento import (dosis_medicamento, eliminar_dosis,
agregar_medicamento, busqueda_medicamento, autocompletado_medicamento)
from modulo_expediente.views.ReferenciaMedica import (ReferenciaMedicaView,
ReferenciaMedicaUpdate, ReferenciaMedicaPdfView)
from modulo_expediente.views.RecetaMedica import RecetaMedicaPdfView
from modulo_expediente.views.DocumentosExternos import ExamenesExternosCreateView, DocumentosExternosURLview, DocumentosExternosURLDownload
from modulo_expediente.views.ContieneConsulta import (agregar_cola,get_cola ,eliminar_cola, consultarRegistroConsultas )
from modulo_expediente.views.Agenda import (CitaConsultaView, AgendaView, CitaConsultaUpdate)
from modulo_expediente.views.ControlSubsecuente import (ControlSubsecuenteView,ControlSubsecuenteConsultaView)
from modulo_expediente.views.RecetaExamen import(RecetaExamenView, RecetaExamenUpdate)

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
    path('signos-vitales/<int:id_consulta>',crear_signos_vitales, name='crear_signos_vitales'),
    path('signos-vitales/<int:id_consulta>/lista',get_signos_vitales, name='lista_signos_vitales'),
    # Antecedentes
    path('consulta/<int:id_expediente>/antecedentes-personales/',antecedentesUpdateView.as_view(),name='antecedentes-update'),
    path('consulta/<int:id_consulta>/receta-medica/pdf',RecetaMedicaPdfView.as_view(),name='receta-medica-pdf' ),
    # Constancias Medicas
    path('consulta/<int:id_consulta>/constancia-medica/',ConstanciaMedicaView.as_view(),name='constancia-medica'),
    path('consulta/<int:id_consulta>/constancia-medica/pdf/<int:id_constancia>/', ConstanciaMedicaPDFView.as_view(),name='constancia-medica'),
    path('consulta/<int:id_consulta>/constancia-medica/<int:id_constancia>/',ConstanciaMedicaUpdate.as_view(),name='constancia-medica-update'),
    #path('constancia-medica/<str:id>',ConstanciaMedicaView.as_view(),name='constancia-medica'),
    path('constancia-medica/',ConstanciaMedicaCreate.as_view(),name='crear-constancia-medica'),
    # Referencias Medicas
    path('consulta/<int:id_consulta>/referencia-medica/',ReferenciaMedicaView.as_view(),name='referencia-medica'),
    path('consulta/<int:id_consulta>/referencia-medica/pdf/<int:id_referencia_medica>/',ReferenciaMedicaPdfView.as_view(),name='referencia-medica-pdf' ),
    path('consulta/<int:id_consulta>/referencia-medica/<int:id_referencia>/',ReferenciaMedicaUpdate.as_view(),name='referencia-medica-update'),
    #Receta Examen
    path('consulta/<int:id_consulta>/receta-examen/',RecetaExamenView.as_view(),name='receta-examen'),
    path('consulta/<int:id_consulta>/receta-examen/<int:id_receta_examen>',RecetaExamenUpdate.as_view(),name='receta-examen-update'),
    # Medicamentos
    path('receta_medica/agregar-medicamento', agregar_medicamento, name='agregar_nuevo_medicamento'),
    path('receta/dosis',dosis_medicamento,name='agregar_dosis'),
    path('receta/dosis/eliminar_dosis/<int:id_dosis>',eliminar_dosis,name='eliminar_dosis'),
    path('medicamento/',busqueda_medicamento, name='agregar_medicamento'),
    path('medicamento/autocompletado/',autocompletado_medicamento, name='agregar_medicamento_2'),
    # Consulta Medica
    path('consulta/<int:id_consulta>/',ConsultaView.as_view(),name='editar_consulta'),
    path('consulta/seguimiento/<int:id_contiene_consulta>/',ConsultaView.as_view(),name='seguimiento_consulta'),
    path('consulta/nueva/<int:id_contiene_consulta>/',ConsultaView.as_view(),name='nueva_consulta'),
    # Evolucion Consulta
    path('consulta/<int:id_consulta>/hoja-evolucion/',CreateHojaEvolucion.as_view(),name='hoja-evolucion-create'),
    path('consulta/<int:id_consulta>/hoja-evolucion/<int:id_nota_evolucion>',DeleteNotaEvolucion.as_view(),name='hoja-evolucion-delete'),
    path('consulta/<int:id_consulta>/hoja-evolucion/update',UpdateNotaEvolucion.as_view(),name='hoja-evolucion-update'),
    path('consulta/<int:id_consulta>/hoja-evolucion/lista',ListaHojaEvolucion.as_view(),name='hoja-evolucion-lista'),
    # Control Subsecuente
    path('consulta/<int:id_consulta>/control-subsecuente/',ControlSubsecuenteView.as_view(),name='control-subsecuente-view'),
    path('consulta/<int:id_consulta>/control-subsecuente/detalle',ControlSubsecuenteConsultaView.as_view(),name='control-subsecuente-consulta-view'),
    # Agenda
    path('agenda/', AgendaView.as_view(),name='ver_agenda'),
    path('consulta/<int:id_consulta>/programar-cita/<int:id_expediente>', CitaConsultaView.as_view(), name='crear-cita-consulta'),
    path('citas-consulta/', CitaConsultaView.as_view(), name='get-citas-consulta'),
    path('citas-consulta/<int:id_cita_consulta>', CitaConsultaUpdate.as_view(), name='view-cita-consulta'),

    ###URL de Pruebas para visualización de archivos en S3
   # path('documento/<int:id_documento>/', storageurl, name="storage-url")
    path('consulta/<int:id_consulta>/agregar-documento-externo/', ExamenesExternosCreateView.as_view(), name="create_examenes_externos"),
    path('documento/<int:id_documento>/', DocumentosExternosURLview.as_view(), name="storage-url"),
    path('documento/download/<int:id_documento>/', DocumentosExternosURLDownload.as_view(), name="download-url"),
    
    #Registro masivo de expedientes
    path('registro-masivo/', RegistroMasivoExpedientesView.as_view(), name="registro_masivo_expedientes"),

    ##SGI
    path('sgi/consultas', consultarRegistroConsultas, name="sgi_consultas"),
]

