from django.contrib import admin
from .models import *

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ['vehicleNumber', 'city', 'category', 'driverName', 'available']
    search_fields = ['vehicleNumber',]

class BookAmbulanceModelAdmin(admin.ModelAdmin):
    list_display = ['ambulance', 'patient', 'date', 'time', 'patientContact']
    search_fields = ['ambulance', 'patient', 'date', 'time', 'patientContact']

admin.site.register(Ambulance, AmbulanceAdmin)
admin.site.register(BookAmbulanceModel, BookAmbulanceModelAdmin)
