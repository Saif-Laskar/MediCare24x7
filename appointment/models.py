from django.db import models
from accounts.models import PatientModel, DoctorModel

# Create your models here.

class AppointmentModel(models.Model):
    patient         = models.ForeignKey(PatientModel, on_delete=models.CASCADE) 
    doctor          = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    department      = models.CharField(null =True, max_length=250)
    date            = models.DateField(null=True, blank=False)
    time            = models.TimeField(null=True, blank=False)
    is_accepted     = models.BooleanField(default=False)
    is_canceled     = models.BooleanField(default=False)
    is_completed    = models.BooleanField(default=False)
    meet_link       = models.CharField(max_length=100)
    notes           = models.TextField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)


class PrescriptionModel(models.Model):
    appointment     = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
    description    = models.TextField(null= True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)