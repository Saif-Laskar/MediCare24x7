from django.contrib import admin
from .models import *


admin.site.register(UserModel)
admin.site.register(PatientModel)
admin.site.register(DoctorModel)