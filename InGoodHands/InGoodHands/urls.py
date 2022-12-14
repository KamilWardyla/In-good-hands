"""InGoodHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from charity_donation.views import LoginUserView, LandingPageView, DonationCreate, AddDonationFormConfirmation, \
    AddUserView, LoginUserView, logout_view, UserDetailsView, UserDonationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginUserView.as_view(), name="login"),
    path('register/', AddUserView.as_view(), name="register"),
    path('', LandingPageView.as_view(), name="landing_page"),
    path('add_donation/', DonationCreate.as_view(), name="add_donation"),
    path('add_donation_confirm/', AddDonationFormConfirmation.as_view(), name="form_confirmation"),
    path('logout', logout_view, name="logout"),
    path('user_details', UserDetailsView.as_view(), name="user_details"),
    path('dontation_details', UserDonationView.as_view(), name="user_donation")
]
