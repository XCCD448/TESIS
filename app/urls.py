from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import logins, Carreras, Ciudades, Contacto, Facultades, Index, Malla, PerfilesU, Ramos, Sedes, Usuarios, RamoC, listar_usuarios, listar_carreras, listar_ciudades, listar_facultades, modificar_usuario, eliminar_usuario, registro, menuadmin, menuestudiannte

urlpatterns = [
    path('Carreras', Carreras, name="Carreras"),
    path('Ciudades', Ciudades, name="Ciudades"),
    path('Contacto', Contacto, name="Contacto"),
    path('Facultades', Facultades, name="Facultades"),
    path('', Index, name="Index"),
    path('login', logins, name="login"),
    path('Malla.html', Malla, name="Malla"),
    path('PerfilesU', PerfilesU, name="PerfilesU"),
    path('RamoC', RamoC, name="RamoC"),
    path('Ramos', Ramos, name="Ramos"),
    path('Sedes', Sedes, name="Sedes"),
    path('Usuario', Usuarios, name="Usuario"),
    path('listar_usuarios/', listar_usuarios, name="listar_usuarios"),
    path('listar_carreras/', listar_carreras, name="listar_carreras"),
    path('listar_ciudades/', listar_ciudades, name="listar_ciudades"),
    path('listar_facultades/', listar_facultades, name="listar_facultades"),
    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
    path('registro/', registro, name="registro"),
    path('menuadmin', menuadmin, name="menuadmin"),
    path('menuestudiante', menuestudiannte, name="menuestudiante"),

    ]