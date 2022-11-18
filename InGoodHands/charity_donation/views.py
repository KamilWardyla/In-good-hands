from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from .models import Donation, Institution
from django.urls import reverse_lazy


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class LandingPageView(View):
    def get(self, request):
        sum_of_bags = 0
        all_bags = Donation.objects.all().values('quantity')
        bags_list = list(all_bags)
        for bag in bags_list:
            sum_of_bags += int(bag['quantity'])
        all_institution = Institution.objects.all().values('name')
        institution_length = len(list(all_institution))
        ctx = {"bags_length": sum_of_bags, "institution_length": institution_length}
        return render(request, 'index.html', ctx)


class AddDonation(CreateView):
    model = Donation
    fields = "__all__"
