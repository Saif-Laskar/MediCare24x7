from django.urls import path
from .views import *

urlpatterns = [
    path('doctorList', appointment_doctorList_view, name='doctorList'),
    path('make-appointment/<int:pk>', make_appointment_view, name='make-appointment'),
    path('detail/<int:pk>', appointment_detail_view, name='appointment-detail'),
    path('all-appointments', patient_all_appointments_view, name='patient-all-appointments'),
    path('doctor-all-appointments', doctor_all_appointments_view, name='doctor-all-appointments'),
    path('update-appointment/<int:pk>', patient_update_appointment_view, name='patient-update-appointment'),
    path('doctor-update-appointment/<int:pk>', doctor_update_appointment_view, name='doctor-update-appointment'),
]