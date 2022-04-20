from django.urls import path
from .views import *

urlpatterns=[
    path('add-ambulance/', add_ambulance_view, name='add-ambulance'),
    path('staff-all-ambulance/', staff_abmulance_view, name='staff-all-ambulance'),
    path('ambulance/ambulance-details/<str:pk>', ambulance_detail_view, name='ambulance-details'),
]