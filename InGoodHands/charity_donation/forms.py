from django.forms import ModelForm
from django import forms
from .models import Donation, User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.core.exceptions import ValidationError


class DonationForm(ModelForm):
    @staticmethod
    def date_validator(value):
        today = datetime.datetime.now().date()
        if value < today:
            raise ValidationError(
                "Nieprawidłowa data, odbiór może nastąpić następnego dnia roboczego"
            )

    pick_up_date = forms.DateField(validators=[date_validator])

    class Meta:
        model = Donation
        fields = "__all__"


class AddUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name")


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")
