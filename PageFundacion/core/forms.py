from django import forms
from django.forms import ModelForm, fields
from.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','email','password','relacion']

class InicioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','password']