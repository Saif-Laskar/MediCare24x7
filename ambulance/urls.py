from django.urls import path
from .views import *

urlpatterns=[
    path('add-ambulance/', add_ambulance_view, name='add-ambulance'),
]