#Python
#Django
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from datetime import datetime

#Librerias Propias
from ..models import Resultado, Categoria
from ..serializers import ResultadoLaboratorioSerializer, RefusultadoSerializerSGI, CategoriaExamenSerializerSGI

#Clase para ver la bitacora
class BitacoraView(PermissionRequiredMixin,TemplateView):
    permission_required = ('modulo_laboratorio.change_resultado')
    template_name = "laboratorio/bitacora.html"
    login_url='/login/'  
    response={'type':'','data':'', 'info':''}

    def post(self, request, *args, **kwargs):
        fecha=timezone.now()
        resultados=Resultado.objects.filter(fecha_hora_toma_de_muestra__year=fecha.year
            ,fecha_hora_toma_de_muestra__month=fecha.month).select_related('orden_de_laboratorio__expediente__id_paciente').order_by('numero_cola_resultado')
        resultados=ResultadoLaboratorioSerializer(resultados,many=True)
        
        self.response['info']=resultados.data

        return JsonResponse(self.response)

def consultarRegistroLaboratorios(request):
    #Recuperando la Fecha
    #try:
        fechaInicio=request.GET.get('fechaInicio','')
        fechaFin=request.GET.get('fechaFin','')
        fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d").date()
        fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d").date()
        queryConsultas=Resultado.objects.filter(fecha_creacion__range=(fechaInicio, fechaFin))
        resultado=RefusultadoSerializerSGI(queryConsultas, many=True)

        response={
                'type':'success',
                'title':'Informe generado',
                'data':resultado.data
            }
        return JsonResponse( response, safe=False)

def consultarCategoriasExamen(request):
    categorias=Categoria.objects.all()
    categorias=CategoriaExamenSerializerSGI(categorias, many=True)
    response={
                'type':'success',
                'title':'Informe generado',
                'data':categorias.data
            }
    return JsonResponse( response, safe=False)

