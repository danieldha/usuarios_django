from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

from usuarios.models import Usuario


class CrearUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'password1',
            'password2',
        )


class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'pdf_file',
            'pdf_file_2'
        )
        field_classes = {'username': UsernameField}