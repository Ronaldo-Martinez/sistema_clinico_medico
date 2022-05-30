from datetime import datetime
from pyexpat import model
from secrets import choice
from unittest.mock import DEFAULT
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.
class Expediente(models.Model):
    
    id_expediente = models.AutoField(primary_key=True, unique=True)
    id_paciente=models.OneToOneField('Paciente', models.CASCADE, blank=False, null=False)
    fecha_creacion_expediente = models.DateField(default=datetime.now,blank=False,null=False)
    codigo_expediente=models.CharField(max_length=10,blank=False,null=False,unique=True)
    contiene_consulta=models.ManyToManyField('Consulta',through='contieneConsulta')#blank=False,null=False, no se utilizan en ManyToMany fields.W122
    def __str__(self):
        return str(self.id_expediente)+" - "+str(self.id_paciente.nombre_paciente)

class Paciente(models.Model):
    OPCIONES_SEXO=(
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    id_paciente=models.AutoField(primary_key=True,unique=True)
    
    nombre_paciente = models.CharField( max_length=40,blank=False, null=False)
    apellido_paciente = models.CharField( max_length=40,blank=False, null=False)
    fecha_nacimiento_paciente = models.DateField( blank=False,null=False)
    sexo_paciente = models.CharField( max_length=1,choices=OPCIONES_SEXO, blank=False, null=False )
    direccion_paciente=models.CharField( max_length=120, blank=True,null=True,default="")
    email_paciente = models.EmailField( max_length=100, blank=False, null=False, unique=True,default="")
    responsable=models.CharField(max_length=40,blank=True,null=True,default='')
    
    def __str__(self):
        return str(self.id_paciente)+" - "+str(self.nombre_paciente)

class ContieneConsulta(models.Model):
    OPCIONES_ESTADO_DE_PAGO=(
        ('1','Pendiente'),
        ('2','Parcialmente pagado'),
        ('3','Pagado'),
    )
    OPCIONES_FASE=(
        ('1','Agendado'),
        ('2','Anotado'),
        ('3','Preparado'),
        ('4','En espera'),
        ('5','En consulta'),
        ('6','Finalizado'),
    )
    #Me parece que el ManyToManyField, no se ocupa en la clase asociación, si no en la clase dominante.
    #expediente = models.ManyToManyField(Expediente, models.DO_NOTHING, blank=False, null=True)
    #consulta = models.ManyToManyField(Consulta, models.DO_NOTHING, blank=False, null=True)
    id=models.AutoField(primary_key=True)
    expediente = models.ForeignKey('Expediente', models.DO_NOTHING, blank=False, null=True)
    consulta = models.OneToOneField('Consulta', models.DO_NOTHING, blank=True, null=True)
    numero_cola=models.IntegerField(blank=False, null=False) #No lleva max_length
    fecha_de_cola=models.DateField(default=datetime.now, blank=False, null=False)
    # hora_de_ingreso=models.TimeField(default=datetime.now,blank=False,null=False)
    consumo_medico=models.DecimalField(max_digits=6,decimal_places=2,null=False, blank=False,default=0)
    estado_cola_medica=models.CharField(max_length=20,choices=OPCIONES_ESTADO_DE_PAGO, blank=False,null=False,default=1)
    fase_cola_medica=models.CharField(max_length=20,choices=OPCIONES_FASE, blank=False,null=False,default=2)
    class Meta:
        unique_together = (('expediente', 'fecha_de_cola'),)

class SignosVitales(models.Model):
    UNIDADES_TEMPERATURA=(
        ('F','Fahrenheit'),
        ('C','Celsius'),
    )
    UNIDADES_PESO=(
        ('Lbs','Libras'),
        ('Kgs','Kilogramos'),
    )
    id_signos_vitales= models.AutoField(primary_key=True)
    #consulta=models.ForeignKey(Consulta,on_delete=models.DO_NOTHING,null=False, blank=False)
    enfermera=models.ForeignKey('modulo_control.Enfermera',on_delete=models.DO_NOTHING,null=True, blank=True)
    unidad_temperatura=models.CharField(max_length=1,choices=UNIDADES_TEMPERATURA,null=False, blank=True,default=2)
    unidad_peso=models.CharField(max_length=3,choices=UNIDADES_PESO,null=False, blank=True,default=1)
    unidad_presion_arterial_diastolica=models.CharField(max_length=4,default='mmHH',null=True, blank=True)
    unidad_presion_arterial_sistolica=models.CharField(max_length=4,default='mmHH',null=True, blank=True)
    unidad_frecuencia_cardiaca=models.CharField(max_length=3,null=False, blank=True,default='PPM')
    unidad_saturacion_oxigeno=models.CharField(max_length=1,default='%',null=False, blank=True)
    valor_temperatura=models.DecimalField(max_digits=5,decimal_places=2,validators=[MaxValueValidator(50),MinValueValidator(15)],null=True, blank=True)
    valor_peso=models.DecimalField(max_digits=5,decimal_places=2,validators=[MaxValueValidator(500),MinValueValidator(0)],null=True, blank=True)
    valor_presion_arterial_diastolica=models.IntegerField(validators=[MaxValueValidator(250),MinValueValidator(0)],null=True, blank=True)
    valor_presion_arterial_sistolica=models.IntegerField(validators=[MaxValueValidator(350),MinValueValidator(0)],null=True, blank=True)
    valor_frecuencia_cardiaca=models.IntegerField(validators=[MaxValueValidator(250),MinValueValidator(0)],null=True, blank=True)
    valor_saturacion_oxigeno=models.IntegerField(validators=[MaxValueValidator(101),MinValueValidator(0)],null=True, blank=True)
    #Cuando se utiliza integerField, Django ignora el max_length, fields.w122

class Consulta(models.Model):
    id_consulta= models.AutoField(primary_key=True)
    signos_vitales= models.OneToOneField('SignosVitales',on_delete=models.DO_NOTHING,null=False, blank=False)
    diagnostico=models.TextField(max_length=200, blank=True, null=False)
    sintoma=models.TextField(max_length=200, blank=True, null=False)

class OrdenExamenLaboratorio(models.Model):
    id_orden_examen_laboratorio= models.AutoField(primary_key=True)
    fecha_programada=models.DateField(default=datetime.now,null=False, blank=False)
    consulta=models.ForeignKey('Consulta',on_delete=models.DO_NOTHING,null=False, blank=False)
    examen_de_laboratorio=models.ForeignKey('modulo_laboratorio.ExamenLaboratorio',on_delete=models.DO_NOTHING,null=False, blank=False)

class Hospital(models.Model):
    id_hospital= models.AutoField(primary_key=True)
    codigo_hospital=models.CharField(max_length=25)
    nombre_hospital=models.CharField(max_length=50)
    telefono_hospital=models.CharField(max_length=9)
    codigo_pais=models.CharField(max_length=3)

class ReferenciaMedica(models.Model):
    id_referencia_medica= models.AutoField(primary_key=True)
    consulta=models.ForeignKey('Consulta',models.DO_NOTHING,null=False, blank=False)
    hospital=models.ForeignKey(Hospital,models.DO_NOTHING,null=False, blank=False)
    especialidad=models.CharField(max_length=30,null=False, blank=False)
    fecha_referencia=models.DateField(default=datetime.now,null=False, blank=False)



class RecetaMedica(models.Model):
    id_receta_medica= models.AutoField(primary_key=True)
    Consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE,null=False, blank=False)

class Medicamento(models.Model):
    PRESENTACION_MEDICAMENTO=(
    ('1','Frasco'),
    ('2','Ampolla'),
    ('3','Frasco vial'),
    ('4','Sobre'),
    ('5','Jeringa prellenada'),
    ('6','Bolsa'),
    ('7','Tubo'),
    ('8','Tarro'),
    ('9','Dispositivo precargado'),
    ('10','Pluma multidosis'),
    ('11','Cartucho'),
    ('12','Frasco gotero'),
    ('13','Capsulas'),
    ('14','Spray'),
    ('15','Suspensión'),
    )
    UNIDADES_DE_MEDIDA_MEDICAMENTO=(
    ('L','litro'),
    ('mL','mililitro'),
    ('µL','microlitro'),
    ('cc / cm³','centímetro cúbico'),
    ('fl oz',	'onza líquida'),
    ('Kg','kilogramo'),
    ('g','gramo'),
    ('mg','miligramo'),
    ('oz','onza'),
    ('capsulas','cápsulas'),
    )
    id_medicamento= models.AutoField(primary_key=True)
    nombre_comercial=models.CharField(max_length=50,null=False, blank=False)
    nombre_generico=models.CharField(max_length=25,null=False, blank=False)
    cantidad_medicamento=models.DecimalField(max_digits=6,decimal_places=2,null=False, blank=False)
    unidad_medicamento=models.CharField(max_length=8,choices=UNIDADES_DE_MEDIDA_MEDICAMENTO,null=False, blank=False)
    presentacion=models.CharField(choices=PRESENTACION_MEDICAMENTO,null=False,blank=False,default=PRESENTACION_MEDICAMENTO[12][0],max_length=25)
    def __str__(self):
        if(self.nombre_comercial):
            return self.nombre_generico+" - "+self.nombre_comercial+" - "+self.PRESENTACION_MEDICAMENTO[int(self.presentacion)][1]
        else:
            return self.nombre_generico+" - "+self.PRESENTACION_MEDICAMENTO[int(self.presentacion)][1]

class Dosis(models.Model):
    OPCIONES_TIEMPO = (
        ('h', 'Hora(s)'),
        ('d', 'Dia(s)'),
        ('s', 'Semana(s)'),
        ('m', 'Mes(es)'),
    )
   
    UNIDADES_DE_MEDIDA_DOSIS = (
        ('got',	'gota'),
        ('mgota / µgota', 'microgota'),
        ('L', 'litro'),
        ('mL', 'mililitro'),
        ('µL', 'microlitro'),
        ('cc / cm³', 'centímetro cúbico'),
        ('fl oz','onza líquida'),
        ('cdita','cucharadita'),
        ('cda','cucharada'),
        ('Kg','kilogramo'),
        ('g','gramo'),
        ('mg','miligramo'),
        ('oz','onza'),
        ('disparos','disparos'),
        ('capsulas','cápsulas'),
    )
    id_dosis= models.AutoField(primary_key=True)
    periodo_dosis=models.IntegerField(null=False,blank=False,default=7)
    unidad_periodo_dosis=models.CharField(max_length=6,choices=OPCIONES_TIEMPO,null=False,blank=False,default=OPCIONES_TIEMPO[1][0])
    frecuencia_dosis=models.IntegerField(null=False,blank=False,default=8)
    unidad_frecuencia_dosis=models.CharField(max_length=6,choices=OPCIONES_TIEMPO,null=False,blank=False,default=OPCIONES_TIEMPO[0][0])
    cantidad_dosis=models.DecimalField(decimal_places=2,max_digits=5,null=False,blank=False,default=1)
    unidad_de_medida_dosis=models.CharField(choices=UNIDADES_DE_MEDIDA_DOSIS,max_length=17,null=False,blank=False,default=UNIDADES_DE_MEDIDA_DOSIS[14][0])
    medicamento=models.OneToOneField(Medicamento,on_delete=models.DO_NOTHING,null=False, blank=False)
    receta_medica=models.ForeignKey(RecetaMedica,on_delete=models.DO_NOTHING,null=False, blank=False)

class BrindaConsulta(models.Model):
    OPCIONES_TURNO=(
        (1,'Matutino'),
        (2,'Vespertino'),
    )
    consulta=models.ForeignKey('Consulta', models.DO_NOTHING, blank=False, null=False)
    doctor=models.ForeignKey('modulo_control.Doctor', models.DO_NOTHING, blank=False, null=False)
    #consultorio=models.IntegerField(blank=False, null=False)#Es llave foranea, pero no existe la clase consultorio
    turno=models.CharField(max_length=20,choices=OPCIONES_TURNO, blank=False,null=False)

class ConstanciaMedica(models.Model):
    id_constancia_medica= models.AutoField(primary_key=True)
    consulta= models.ForeignKey('Consulta', models.DO_NOTHING, blank=False, null=False)
    fecha_de_emision=models.DateField(default=datetime.now, blank=False, null=False)
    dias_reposo=models.IntegerField(blank=False, null=False)#Los integer no llevan max_length
    diagnostico_constancia=models.CharField(max_length=200, blank=False, null=False)
