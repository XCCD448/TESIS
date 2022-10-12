from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import eliminar_carreras, logins, Carreras, Ciudades, Contacto, Facultades, Index, Malla, PerfilesU, Ramos, Sedes, Usuarios, RamoC, listar_usuarios, listar_carreras, listar_ciudades, listar_facultades, modificar_carreras, modificar_facultades, modificar_usuario, eliminar_usuario, registro, menuadmin, menuestudiannte, eliminar_facultades, modificar_ciudades, eliminar_ciudades, listar_ramos, modificar_ramos, eliminar_ramos, listar_mallas, modificar_mallas, eliminar_mallas, listar_sedes, modificar_sedes, eliminar_sedes

urlpatterns = [
    path('Carreras', Carreras, name="Carreras"),
    path('modificar_carreras/<id>/', modificar_carreras, name="modificar_carreras"),
    path('eliminar_carreras/<id>/', eliminar_carreras, name="eliminar_carreras"),
    path('Ciudades', Ciudades, name="Ciudades"),
    path('modificar_ciudades/<id>/', modificar_ciudades, name="modificar_ciudades"),
    path('eliminar_ciudades/<id>/', eliminar_ciudades, name="eliminar_ciudades"),
    path('Contacto', Contacto, name="Contacto"),
    path('Facultades', Facultades, name="Facultades"),
    path('', Index, name="Index"),
    path('login', logins, name="login"),
    path('Malla.html', Malla, name="Malla"),
    path('listar_mallas/', listar_mallas, name="listar_mallas"),
    path('modificar_mallas/<id>/', modificar_mallas, name="modificar_mallas"),
    path('eliminar_mallas/<id>/', eliminar_mallas, name="eliminar_mallas"),
    path('PerfilesU', PerfilesU, name="PerfilesU"),
    path('RamoC', RamoC, name="RamoC"),
    path('Ramos', Ramos, name="Ramos"),
    path('Sedes', Sedes, name="Sedes"),
    path('listar_sedes/', listar_sedes, name="listar_sedes"),
    path('modificar_sedes/<id>/', modificar_sedes, name="modificar_sedes"),
    path('eliminar_sedes/<id>/', eliminar_sedes, name="eliminar_sedes"),
    path('listar_ramos/', listar_ramos, name="listar_ramos"),
    path('modificar_ramos/<id>/', modificar_ramos, name="modificar_ramos"),
    path('eliminar_ramos/<id>/', eliminar_ramos, name="eliminar_ramos"),
    path('Usuario', Usuarios, name="Usuario"),
    path('listar_usuarios/', listar_usuarios, name="listar_usuarios"),
    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
    path('listar_carreras/', listar_carreras, name="listar_carreras"),
    path('listar_ciudades/', listar_ciudades, name="listar_ciudades"),
    path('listar_facultades/', listar_facultades, name="listar_facultades"),
    path('modificar_facultades/<id>/', modificar_facultades, name="modificar_facultades"),
    path('eliminar_facultades/<id>/', eliminar_facultades, name="eliminar_facultades"),
    path('registro/', registro, name="registro"),
    path('menuadmin', menuadmin, name="menuadmin"),
    path('menuestudiante', menuestudiannte, name="menuestudiante"),

    ]