from django import forms
from django.forms import SelectDateWidget
from .models import Plan, Recipe, RecipePlan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nazwa planu'}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Opis planu'}),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'preparation_time', 'preparation_description', 'ingredients')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nazwa przepisu'}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Opis przepisu'}),
            'ingredients': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Składniki'}),
            'preparation_description': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Opis '                                                                                            'przygotowania'}),
        }


class RecipePlanForm(forms.ModelForm):
    class Meta:
        model = RecipePlan
        fields = ('plan', 'meal_name', 'recipe', 'day')


class RecipeVotesForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('votes',)
