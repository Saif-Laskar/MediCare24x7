from django.db import models
from accounts.models import PatientModel, DoctorModel

# Create your models here.

class AppointmentModel(models.Model):
    patient         = models.ForeignKey(PatientModel, on_delete=models.CASCADE) 
    doctor          = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    date            = models.DateField()
    time            = models.TimeField()
    reason          = models.TextField()
    status          = models.CharField(max_length=10, default='Pending')
    is_accepted     = models.BooleanField(default=False)
    is_canceled     = models.BooleanField(default=False)
    is_completed    = models.BooleanField(default=False)
    meet_link       = models.CharField(max_length=100)
    created_at      = models.DateTimeField(auto_now_add=True)


class PrescriptionModel(models.Model):
    appointment     = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
    prescription    = models.TextField(null= True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)