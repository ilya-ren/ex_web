from django import forms
from .models import Obra
from django.forms import ModelForm

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = "__all__"