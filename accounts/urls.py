from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),

    path('accounts/login', login_view, name='login'),  # login
    path('accounts/logout', logout_view, name='logout'),  # logout
    path('accounts/patient-signup', patient_signup_view, name='signup'),  # patient registration


    path('accounts/patient-dashboard', patient_dashboard_view, name='patient-dashboard'),# patient dashboard
    path('accounts/patient-profile', patient_profile_view, name='patient-profile'),

]

