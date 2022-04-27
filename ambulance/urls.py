from django.urls import path
from .views import *

urlpatterns=[
    path('add-ambulance/', add_ambulance_view, name='add-ambulance'),
    path('staff-all-ambulance/', staff_abmulance_view, name='staff-all-ambulance'),
    path('ambulance/ambulance-details/<str:pk>', ambulance_detail_view, name='ambulance-details'),

    path('ambulance/edit-ambulance-details/<str:pk>', edit_ambulance_view, name='edit-ambulance-details'),
    path('patient-available-abmulance/', patient_available_abmulance_view, name='patient-available-abmulance'),
    path('ambulance-booking/<str:pk>', ambulance_booking_view,name= 'ambulance-booking'),

    path('cinfirm-ambulance-booking/<str:pk>', confirm_ambulance_booking_view, name='cinfirm-ambulance-booking'),

]