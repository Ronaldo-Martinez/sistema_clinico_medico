from cgitb import text
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import datetime

def crear_codigo(nombres,apellidos):
        year=datetime.datetime.now().date().strftime("%Y")[2:]
        texto=nombres[0]+apellidos[0]
        texto=texto.lower()#Solo texto en minusculas
        texto=texto+year
        
        try:
            correlativo = correlativo = Empleado.objects.filter(codigo_empleado__startswith=texto).last().codigo_empleado
            correlativo=int(correlativo[4:])
        except:
            correlativo=0
        
        correlativo=correlativo+1
        if correlativo < 10:
            correlativo="00"+str(correlativo)
        elif correlativo < 100:
            correlativo = "0"+str(correlativo)
        #Codigo de Usuario al estilo -- mv17012 ---
        codigo=texto+correlativo
        return codigo

class EmpleadoManager(BaseUserManager):
    def create_user(self, nombres,apellidos,email,password = None):
        if not email:
            raise ValueError('El Usuario debe tener un correo')
        
        #Codigo Usuario 
        codigo=crear_codigo(nombres, apellidos)
        #Codigo de Usuario al estilo -- mv17012 ---
        #----- No se como hacer si se registra alguien con tilde en el primer apellido ----
        #----- Pero es poco probable que ocurra :P -----------------------

        #Crear usuario
        empleado=self.model(
            codigo_empleado=codigo,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )

        empleado.set_password(password)
        empleado.save()
        return empleado
    
    def create_superuser(self, nombres,apellidos,email, password = None):
        empleado=self.create_user(
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )
        empleado.es_activo=True
        empleado.es_staff = True
        empleado.es_superuser=True
        empleado.save()
        return empleado


class Empleado(AbstractBaseUser, PermissionsMixin):
    codigo_empleado = models.CharField(primary_key=True,max_length=7,unique=True)
    nombres = models.CharField(db_column='NOMBRES', max_length=40, null=True)
    apellidos = models.CharField(db_column='APELLIDOS', max_length=40, null=True)
    sexo = models.CharField(db_column='SEXO', max_length=1, default='-')
    direccion=models.CharField(db_column='DIRECCION', max_length=120, null=True)
    email = models.EmailField(db_column='EMAIL', max_length=100, blank=True, null=True, unique=True)
    es_activo = models.BooleanField(db_column='ES_ACTIVO', default=True)
    es_staff = models.BooleanField(db_column='ES_STAFF', default=False)
    es_superuser = models.BooleanField(db_column='IS_SUPERUSER', default=False)
    last_login = models.DateField(db_column='LAST_LOGIN', null=True)
    fechaCreacion = models.DateTimeField(db_column='FECHA_CREACION', default=timezone.now)
    fechaNacimiento = models.DateField(db_column='FECHA_NACMIENTO', null=True)
    objects = EmpleadoManager()

    USERNAME_FIELD="email"
    NAME_FIELD = "nombres"
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    def __str__(self):
        return f'{self.email}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.es_staff  
    @property
    def is_active(self):
        return self.es_activo
    @property
    def is_superuser(self):
        return self.es_superuser