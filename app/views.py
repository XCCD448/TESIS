from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Facultad, Malla_curricular, Ramo, Sede, Usuario, Carrera, Ciudad
from django.contrib import messages
from .forms import ContactoForm, UsuarioForm, SedeForm, CarreraForm, MallaForm, CiudadForm, FacultadForm, PerfilForm, RamoForm, Ramo_carreraForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login


# Create your views here.

@login_required
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

@login_required
def listar_carreras(request):
    Carreras = Carrera.objects.all()

    data = {
        'Carreras': Carreras
    }

    return render(request, 'app/productos/listar_carreras.html', data)

@login_required
def modificar_carreras(request, id):

    carreras = get_object_or_404(Carrera, id=id)

    data={
        'form': CarreraForm(instance=carreras)
    }

    if request.method == 'POST':
        formulario = CarreraForm(data=request.POST, instance=carreras, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_carreras")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_carreras.html', data)

@login_required
def eliminar_carreras(request, id):
    carreras = get_object_or_404(Carreras, id=id)
    carreras.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_carreras")
# -------------------------------------------------------------------------------------------------------------------------
@login_required
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
    
@login_required
def modificar_ciudades(request, id):

    ciudades = get_object_or_404(Ciudad, id=id)

    data={
        'form': CiudadForm(instance=ciudades)
    }

    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST, instance=ciudades, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_ciudades")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_ciudades.html', data)

@login_required
def eliminar_ciudades(request, id):
    ciudades = get_object_or_404(Ciudad, id=id)
    ciudades.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_ciudades")
# -------------------------------------------------
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

@login_required
def Index(request):
    return render(request, 'app/Index.html')

@login_required
def logins(request):
    return render(request, 'registration/login.html')  

@login_required
def Malla(request):
    return render(request, 'app/Malla.html')   

@login_required
def listar_mallas(request):
    Mallas = Malla_curricular.objects.all()

    data = {
        'mallas': Mallas
    }

    return render(request, 'app/productos/listar_mallas.html', data) 

@login_required
def modificar_mallas(request, id):

    Mallas = get_object_or_404(Malla_curricular, id=id)

    data={
        'form': MallaForm(instance=Mallas)
    }

    if request.method == 'POST':
        formulario = MallaForm(data=request.POST, instance=Mallas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_facultades")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_facultades.html', data)

@login_required
def eliminar_mallas(request, id):
    facultad = get_object_or_404(Malla_curricular, id=id)
    facultad.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_facultades")

@login_required
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

@login_required
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

@login_required
def Ramos(request):
    data = {
        'form': RamoForm()
    }

    if request.method == 'POST':
        formulario = RamoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Ramo guardado"
        else:
            data['form'] = formulario
    return render(request, 'app/Ramos.html', data) 

@login_required
@login_required
def listar_ramos(request):
    Ramos = Ramo.objects.all()

    data = {
        'Ramos': Ramos
    }
    return render(request, 'app/productos/listar_ramos.html', data)   

@login_required
def modificar_ramos(request, id):

    ramos = get_object_or_404(Ramo, id=id)

    data={
        'form': RamoForm(instance=ramos)
    }

    if request.method == 'POST':
        formulario = RamoForm(data=request.POST, instance=ramos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_ramos")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_ramos.html', data)

@login_required
def eliminar_ramos(request, id):
    Ramos = get_object_or_404(Ramo, id=id)
    Ramos.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_ramos")
# -------------------------------------------------
@login_required
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

@login_required
def listar_sedes(request):
    Sedes = Sede.objects.all()

    data = {
        'Sedes': Sedes
    }

    return render(request, 'app/productos/listar_sedes.html', data) 

@login_required
def modificar_sedes(request, id):

    Sedes = get_object_or_404(Sede, id=id)

    data={
        'form': SedeForm(instance=Sedes)
    }

    if request.method == 'POST':
        formulario = SedeForm(data=request.POST, instance=Sedes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_sedes")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_sedes.html', data)

@login_required
def eliminar_sedes(request, id):
    facultad = get_object_or_404(Sede, id=id)
    facultad.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_sedes") 

@login_required
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

@login_required
def listar_usuarios(request):
    Usuarios = Usuario.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(Usuarios, 2)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': Usuarios,
        'paginator': paginator
    }

    return render(request, 'app/productos/listar_usuarios.html', data)

@login_required
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
@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_usuarios")

@login_required
def listar_ciudades(request):
    Ciudades = Ciudad.objects.all()

    data = {
        'Ciudades': Ciudades
    }

    return render(request, 'app/productos/listar_ciudades.html', data)    
    
@login_required
def Facultades(request):
    data = {
        'form': FacultadForm()
    }

    if request.method == 'POST':
        formulario = FacultadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Facultad guardada"
        else:
            data['form'] = formulario
    return render(request, 'app/Facultades.html', data)  

@login_required
def listar_facultades(request):
    Facultades = Facultad.objects.all()

    data = {
        'Facultades': Facultades
    }

    return render(request, 'app/productos/listar_facultades.html', data) 

@login_required
def modificar_facultades(request, id):

    facultad = get_object_or_404(Facultad, id=id)

    data={
        'form': FacultadForm(instance=facultad)
    }

    if request.method == 'POST':
        formulario = FacultadForm(data=request.POST, instance=facultad, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificacion correcta")
            return redirect(to="listar_facultades")  
        data['form'] = formulario

    return render(request, 'app/productos/modificar_facultades.html', data)

@login_required
def eliminar_facultades(request, id):
    facultad = get_object_or_404(Facultad, id=id)
    facultad.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_facultades")

def registro(request):
    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al Index
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="Index")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

@login_required
@permission_required('App.add_sessions')
def menuadmin(request):
    return render(request, 'app/menuadmin.html')

@login_required
def menuestudiannte(request):
    return render(request, 'app/menuestudiante.html')    