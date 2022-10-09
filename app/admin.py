from django.contrib import admin
from .models import Carrera, Ciudad, Detalle_malla_carrera, Facultad, Malla_curricular, Perfil, Perfil_permiso, Periodo, Permiso, Planificacion, Ramo, Ramo_carrera, Revision, Sede, Semestre, Trazabilidad, Usuario, Usuario_comision, Usuario_perfil, Contacto

# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    list_display = ["codigo_carrera", "nombre_carrera"]
    search_fields = ["codigo_carrera"]

class CiudadAdmin(admin.ModelAdmin):
    list_display = ["nombre_ciudad"]    
    search_fields = ["nombre_ciudad"]

class FacultadAdmin(admin.ModelAdmin):
    list_display = ["nombre_facultad", "vigente"]    

class MallaCurricularAdmin(admin.ModelAdmin):
    list_display = ["descripcion_malla"]

class PerfilAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "name"]

class PerfilPermisoAdmin(admin.ModelAdmin):
    list_display = ["perfil_id", "permiso_id"]

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["nombre_periodo"]

class PermisoAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "name"]

class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ["fecha_subida", "ruta", "ramo_id", "usuario_id"]

class RamoAdmin(admin.ModelAdmin):
    list_display = ["codigo_ramo", "nombre_ramo", "vigente"]
    search_fields = ["codigo_ramo"] 

class RamoCarreraAdmin(admin.ModelAdmin):
    list_display = ["creditos", "carrera_id", "periodo_id", "ramo_id", "usuario_id"]    

class RevisionAdmin(admin.ModelAdmin):
    list_display = ["comentarios", "estado", "fecha_subida", "planificacion_id", "usuario_id"]

class SedeAdmin(admin.ModelAdmin):
    list_display = ["nombre_sede", "ciudad_id"]
    search_fields = ["ciudad_id"]

class SemestreAdmin(admin.ModelAdmin):
    list_display = ["descripcion_semestre"]

class TrazabilidadAdmin(admin.ModelAdmin):
    list_display = ["accion", "fecha", "usuario_id"]    

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["apellidos", "nombres", "correo", "rut_usuario", "carrera_id"]
    search_fields = ["rut_usuario"]

class UsuarioComisionAdmin(admin.ModelAdmin):
    list_display = ["carrera_id", "usuario_id"]

class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ["usuario_id", "perfil_id"]    

admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Detalle_malla_carrera)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Malla_curricular, MallaCurricularAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Perfil_permiso, PerfilPermisoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Permiso, PermisoAdmin)
admin.site.register(Planificacion, PlanificacionAdmin)
admin.site.register(Ramo, RamoAdmin)
admin.site.register(Ramo_carrera, RamoCarreraAdmin)
admin.site.register(Revision, RevisionAdmin)
admin.site.register(Sede, SedeAdmin)
admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Trazabilidad, TrazabilidadAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Usuario_comision, UsuarioComisionAdmin)
admin.site.register(Usuario_perfil, UsuarioPerfilAdmin)
admin.site.register(Contacto)