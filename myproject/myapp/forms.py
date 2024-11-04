from django import forms
from .models import SimpleModel


class SimpleModelForm(forms.ModelForm):
    class Meta:
        model = SimpleModel
        fields = ['name', 'description']
