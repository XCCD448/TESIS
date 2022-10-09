from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Facultad, Usuario, Carrera, Ciudad
from django.contrib import messages
from .forms import ContactoForm, UsuarioForm, SedeForm, CarreraForm, CiudadForm, FacultadForm, PerfilForm, RamoForm, Ramo_carreraForm

# Create your views here.

def Carreras(request):
    data = {
        'form': CarreraForm()
    }

    if request.method == 'POST':
        formulario = CarreraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario

    return render(request, 'app/Carreras.html', data)

def Ciudades(request):
    data = {
        'form': CiudadForm()
    }

    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/Ciudades.html', data) 

def Contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario

    return render(request, 'app/Contacto.html', data)  

def Facultades(request):
    data = {
        'form': FacultadForm()
    }

    if request.method == 'POST':
        formulario = FacultadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/Facultades.html', data)  

def Index(request):
    return render(request, 'app/Index.html')

def login(request):
    return render(request, 'app/login.html')     

def Malla(request):
    return render(request, 'app/Malla.html')   
    
def PerfilesU(request):
    data = {
        'form': PerfilForm()
    }

    if request.method == 'POST':
        formulario = PerfilForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/PerfilesU.html', data)

def RamoC(request):
    data = {
        'form': Ramo_carreraForm()
    }

    if request.method == 'POST':
        formulario = Ramo_carreraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/RamoC.html', data)    

def Ramos(request):
    data = {
        'form': RamoForm()
    }

    if request.method == 'POST':
        formulario = RamoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/Ramos.html', data) 

def Sedes(request):

    data = {
        'form': SedeForm
    }

    if request.method == 'POST':
        formulario = SedeForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
        else:
            data['form'] = formulario

    return render(request, 'app/Sedes.html', data)    

def Usuarios (request):
    data = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Agregado")
        else:
            data["form"] = formulario
    return render(request, 'app/Usuario.html', data)                    

def listar_usuarios(request):
    Usuarios = Usuario.objects.all()

    data = {
        'Usuarios': Usuarios
    }

    return render(request, 'app/productos/listar_usuarios.html', data)

def listar_carreras(request):
    Carreras = Carrera.objects.all()

    data = {
        'Carreras': Carreras
    }

    return render(request, 'app/productos/listar_carreras.html', data)

def listar_ciudades(request):
    Ciudades = Ciudad.objects.all()

    data = {
        'Ciudades': Ciudades
    }

    return render(request, 'app/productos/listar_ciudades.html', data)    

def listar_facultades(request):
    Facultades = Facultad.objects.all()

    data = {
        'Facultades': Facultades
    }

    return render(request, 'app/productos/listar_facultades.html', data) 


def modificar_usuario(request, id):

    usuario = get_object_or_404(Usuario, id=id)

    data={
        'form': UsuarioForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_usuarios")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_usuario.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_usuarios")