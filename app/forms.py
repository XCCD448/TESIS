from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from turtle import width
from unicodedata import name
from django import forms
from .models import Contacto, Usuario, Sede, Carrera, Ciudad, Facultad, Perfil, Ramo, Ramo_carrera
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validator import MaxSizeFileValidator

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ("nombre", "correo", "tipo_consulta", "mensaje", "avisos")
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class SedeForm(forms.ModelForm):

    class Meta:
        model = Sede
        fields = '__all__'        

class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = '__all__'   

class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = '__all__'   

class FacultadForm(forms.ModelForm):

    class Meta:
        model = Facultad
        fields = '__all__'   

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = '__all__'   

class RamoForm(forms.ModelForm):

    class Meta:
        model = Ramo
        fields = '__all__'   

class Ramo_carreraForm(forms.ModelForm):

    class Meta:
        model = Ramo_carrera
        fields = '__all__'   


class CustomUserCreationForm(UserCreationForm):
    
    

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]









