from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Donation, Institution, User, Category
from django.urls import reverse_lazy
from .forms import AddUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


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


class DonationCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/add_donation/'
    info_sended = False
    model = Donation
    fields = "__all__"
    success_url = reverse_lazy("/add_donation_confirm/")
    template_name = 'form.html'
    all_categories = Category.objects.all()
    all_institution = Institution.objects.all()

    def form_valid(self, form):
        self.info_sended = True
        return super(DonationCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(DonationCreate, self).get_context_data(**kwargs)
        ctx['all_categories'] = self.all_categories
        ctx['all_institution'] = self.all_institution
        return ctx


class AddUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request,
                             "Jesteś aktualnie zalogowany jeśli chcesz stworzyć nowe konto najpierw się wyloguj")
            return redirect('landing_page')
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
            messages.success(request, "Rejestracja zakończona sukcesem!")
            return redirect('login')
        return render(request, 'register.html', ctx)


class LoginUserView(View):
    def get(self, request):
        form = LoginForm
        ctx = {"form": form}
        return render(request, "login.html", ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            messages.warning(request, "Błąd w nazwie użytkownika lub haśle")
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('landing_page')


class UserDetailsView(LoginRequiredMixin, View):
    def get(self, request):
        user_details = User.objects.get(id=request.user.id)
        print(user_details)
        ctx = {"user_details": user_details}
        return render(request, "user_details.html", ctx)


class UserDonationView(LoginRequiredMixin, View):
    def get(self, request):
        donation_details = Donation.objects.filter(user=request.user)
        ctx = {'details': donation_details}
        return render(request, 'donation_details.html', ctx)
