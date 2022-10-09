from datetime import date
from inspect import classify_class_attrs
from pyexpat import model
from random import choices
from django.db import models


# Create your models here.

class Ciudad (models.Model):
    nombre_ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_ciudad

class Sede (models.Model):
    nombre_sede = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre_sede

class Facultad (models.Model):
    nombre_facultad = models.CharField(max_length=255)
    vigente = models.BooleanField()
    sede = models.ForeignKey(Sede, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.nombre_facultad

class Carrera (models.Model):
    codigo_carrera = models.CharField(max_length=255)
    nombre_carrera = models.CharField(max_length=255)
    vigente = models.BooleanField()
    facultad = models.ForeignKey(Facultad, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre_carrera

class Usuario (models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    rut_usuario = models.CharField(max_length=50)
    vigente = models.BooleanField()
    carrera = models.ForeignKey(Carrera, on_delete = models.PROTECT)

    def __str__(self):
        return self.rut_usuario

class Semestre (models.Model):
    descripcion_semestre = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion_semestre

class Malla_curricular (models.Model):
    descripcion_malla = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion_malla

class Ramo (models.Model):
    codigo_ramo = models.CharField(max_length=255)
    nombre_ramo = models.CharField(max_length=255)
    vigente = models.BooleanField()

    def __str__(self):
        return self.codigo_ramo

class Periodo (models.Model):
    nombre_periodo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_periodo

class Perfil (models.Model):
    descripcion = models.CharField(max_length=255)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Permiso (models.Model):
    descripcion = models.CharField(max_length=255)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Trazabilidad (models.Model):
    accion = models.CharField(max_length=255)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

    def __str__(self):
        return self.accion

class Ramo_carrera (models.Model):
    creditos = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete = models.PROTECT)
    periodo = models.ForeignKey(Periodo, on_delete = models.PROTECT)
    ramo = models.ForeignKey(Ramo, on_delete = models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

    def __str__(self):
        return self.creditos

class Planificacion (models.Model):
    fecha_subida = models.DateTimeField()
    ruta = models.CharField(max_length=255)
    ramo = models.ForeignKey(Ramo, on_delete = models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

    def __str__(self):
        return self.fecha_subida

class Revision (models.Model):
    comentarios = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    fecha_subida = models.DateTimeField()
    planificacion = models.ForeignKey(Planificacion, on_delete = models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

    def __str__(self):
        return self.estado

class Detalle_malla_carrera (models.Model):
    carrera = models.ForeignKey(Carrera, on_delete = models.PROTECT)
    malla_curricular = models.ForeignKey(Malla_curricular, on_delete = models.PROTECT)
    ramo = models.ForeignKey(Ramo, on_delete = models.PROTECT)
    semestre = models.ForeignKey(Semestre, on_delete = models.PROTECT)

class Usuario_comision (models.Model):
    carrera = models.ForeignKey(Carrera, on_delete = models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)

class Usuario_perfil (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete = models.PROTECT)

class Perfil_permiso (models.Model):
    perfil = models.ForeignKey(Perfil, on_delete = models.PROTECT)
    permiso = models.ForeignKey(Permiso, on_delete = models.PROTECT)

opciones_consulta = [
    [0, "consultas"],
    [1, "reclamo"],
]

class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre