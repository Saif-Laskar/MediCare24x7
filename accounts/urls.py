from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),

    path('accounts/login', login_view, name='login'),  # login
    path('accounts/logout', logout_view, name='logout'),  # logout
    path('accounts/patient-signup', patient_signup_view, name='signup'),  # patient registration
    
    path('accounts/patient-dashboard', patient_dashboard_view, name='patient-dashboard'),
    path('accounts/patient-profile/<str:pk>', patient_profile_view, name='patient-profile'),
    path('accounts/patient-edit-profile', patient_profile_edit_view, name='patient-edit-profile'),

    path('accounts/doctor-dashboard', doctor_dashboard_view, name='doctor-dashboard'),
    path('accounts/doctor-profile/<str:pk>', doctor_profile_view, name='doctor-profile'),
    path('accounts/doctor-edit-profile', doctor_profile_edit_view, name='doctor-edit-profile'),
    
    path('accounts/staff-dashboard', staff_dashboard_view, name='staff-dashboard'),
    path('accounts/add-doctor', add_doctor_view, name='add-doctor'),
]

