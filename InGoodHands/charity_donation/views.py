from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, FormView
from .models import Donation, Institution, User
from django.urls import reverse_lazy
from .forms import DonationForm, AddUserForm


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
        all_institution = Institution.objects.all()
        all_foundation = all_institution.filter(type='Fundacja')
        all_non_government = all_institution.filter(type="Organizacja pozarządowa")
        all_local_collection = all_institution.filter(type="Lokalna Zbiórka")
        institution_length = len(list(all_institution))
        ctx = {"bags_length": sum_of_bags,
               "institution_length": institution_length,
               "all_institution": all_institution,
               "all_foundation": all_foundation,
               "all_non_government": all_non_government,
               "all_local_collection": all_local_collection
               }
        return render(request, 'index.html', ctx)


class AddDonationFormConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class AddDonation(View):
    def get(self, request):
        form = DonationForm
        ctx = {"form": form}
        return render(request, "form.html", ctx)

    def post(self, request):
        form = DonationForm(request.POST)
        ctx = {"form": form}
        if form.is_valid():
            form.save()
            return redirect('form_confirmation')
        return render(request, "form.html", ctx)


class AddUserView(View):
    def get(self, request):
        form = AddUserForm
        ctx = {"form": form}
        return render(request, 'register.html', ctx)

    def post(self, request):
        form = AddUserForm(request.POST)
        ctx = {"form": form}
        email = request.POST['email']
        if form.is_valid():
            user = form.save(commit=False)
            user.username = email
            user.save()
            return redirect('login')
        return render(request, 'register.html', ctx)
