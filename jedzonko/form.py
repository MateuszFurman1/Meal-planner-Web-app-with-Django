from django import forms
from django.forms import SelectDateWidget
from .models import Plan, Recipe, RecipePlan
from django.contrib.auth.models import User



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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['re_password']:
            raise ValidationError('Passwords are not the same!')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']