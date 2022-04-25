from dataclasses import field
from xml.dom.minidom import Attr
from .models import *
from django.forms import ModelForm
from django import forms




class AmbulanceForm(ModelForm):

    class Meta:
        model = Ambulance
        fields = '__all__'


class AmbulanceEditForm(ModelForm):

    class Meta:
        model = Ambulance  
        fields = '__all__' 
         

class BookAmbulanceForm(ModelForm):

    date = forms.DateField(widget= forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))

    class Meta:
        model = BookAmbulanceModel
        fields = '__all__'
        exclude =['ambulance', 'patient']

