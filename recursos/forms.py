from django import forms
from django.utils import timezone
from recursos.models import *



class RepositorioPageDatosform(forms.ModelForm):
    class Meta: 
        model : RepositorioPageDatos
        fields = [
            "macromedia",
            "visitas",
            "me_gusta",
            "no_megusta"
        ]