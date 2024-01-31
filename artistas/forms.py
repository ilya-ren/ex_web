from django import forms
from .models import Artista
from django.forms import ModelForm

class ArtistaForm(ModelForm):
    class Meta:
        model = Artista
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }