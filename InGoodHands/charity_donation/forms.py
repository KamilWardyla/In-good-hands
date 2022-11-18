from django.forms import ModelForm
from .models import Donation, User
from django.contrib.auth.forms import UserCreationForm


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = "__all__"


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name")
