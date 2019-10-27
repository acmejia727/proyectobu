from entrega.models import *
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class FormInscripcion(forms.ModelForm):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        fields = '__all__'
        exclude = ('estudiante','estado',)      
        model = Registro_estudiante


