from django.forms import ModelForm, TextInput
from django import forms
from .models import Donation, User
from django.contrib.auth.forms import UserCreationForm


class AddUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, min_length=4, required=True, label='Imię',
                                 widget=forms.TextInput(attrs={'placeholder': 'Imię', "div class": 'form-group'}))
    last_name = forms.CharField(max_length=32, min_length=4, required=True, label='Nazwisko',
                                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko', "div class": 'form-group'}))
    email = forms.EmailField(max_length=50, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'email', "div class": 'form-group'}))
    password1 = forms.CharField(label='Hasło',
                                widget=(
                                    forms.PasswordInput(attrs={'placeholder': 'Hasło', ' div class': 'form-group'})))
    password2 = forms.CharField(label='Powtórz Hasło',
                                widget=(forms.PasswordInput(
                                    attrs={'placeholder': 'Powtórz hasło', 'div class': 'form-group'})))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")
