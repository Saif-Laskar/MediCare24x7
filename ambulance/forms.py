from .models import *
from django.forms import ModelForm
from django import forms




class AmbulanceForm(ModelForm):

    class Meta:
        model = Ambulance
        fields = '__all__'