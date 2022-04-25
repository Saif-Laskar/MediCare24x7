from django.contrib import admin
from .models import *

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ['vehicleNumber', 'city', 'category', 'driverName', 'available']
    search_fields = ['vehicleNumber',]



admin.site.register(Ambulance, AmbulanceAdmin)
admin.site.register(BookAmbulanceModel)
