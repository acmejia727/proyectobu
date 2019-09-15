from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *


class UsuarioForm(forms.ModelForm):
    email = forms.CharField(max_length=75, required=True, label="Correo electrónico",
                            widget=forms.TextInput(attrs={'placeholder': 'user@dominio.com'}))
    first_name = forms.CharField(max_length=75, required=True, label="Nombres")
    last_name = forms.CharField(max_length=75, required=True, label="Apellidos")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        cleaned_data = super(UsuarioForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "La contraseña no coincide"
            )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']



class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        fields = ['foto']
        exclude = ('user',)
        model = Personal

