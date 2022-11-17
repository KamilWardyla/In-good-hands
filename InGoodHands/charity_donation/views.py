from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from .models import Donation
from django.urls import reverse_lazy


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddDonation(CreateView):
    model = Donation
    fields = "__all__"
