from django import forms
from django.forms import SelectDateWidget

from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nazwa planu'}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Opis planu'}),
        }