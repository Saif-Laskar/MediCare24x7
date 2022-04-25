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

    date = forms.DateField(widget= forms.DateInput(Attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeField(attrs={'type':'time'}))
    
    class Meta:
        model = BookAmbulanceModel
        field = '__all__'