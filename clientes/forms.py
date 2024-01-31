from django import forms
from .models import Cliente
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }