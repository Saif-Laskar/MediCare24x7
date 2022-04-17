from django.urls import path
from .views import *

urlpatterns = [
    path('doctorList', appointment_doctorList_view, name='doctorList'),

]