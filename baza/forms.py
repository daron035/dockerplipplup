from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TableForm(forms.ModelForm): 
    class Meta:
        model = Detail
        fields = ['name', 'gost']