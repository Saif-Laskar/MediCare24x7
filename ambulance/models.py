from statistics import mode
from unicodedata import category
from django.db import models
from accounts.constants import CITY_CHOICES, TYPES_CHOICES
from accounts.models import PatientModel


class Ambulance(models.Model):  # Ambulance model;
    "Here all the information is about a ambulance including its driver"

    vehicleNumber = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20, choices=CITY_CHOICES, null=False)
    category = models.CharField(max_length=20, choices=TYPES_CHOICES, null=False)
    driverName = models.CharField(max_length=20, null=True, blank=True)
    driverContact = models.CharField(max_length=20, null=True, blank=True)
    driverEmail = models.EmailField(max_length=20, null=True, blank=True)
    driverAddress = models.CharField(max_length=20, null=True, blank=True)
    driverNID = models.CharField(max_length=20, null=True, blank=True, unique=True)
    driverLicense = models.CharField(max_length=20, null=True, blank=True, unique=True)
    driverBloodGroup = models.CharField(max_length=20, null=True, blank=True)
    driverGender = models.CharField(max_length=20, null=True, blank=True)
    driverImage = models.ImageField(null=True, blank=True)
    ambulanceImage = models.ImageField(null=True, blank=True)
    rentInterDivision = models.IntegerField(null=True, blank=True)
    rentIntraDivision = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Ambulances"


class BookAmbulanceModel(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    patientContact = models.CharField(null=False, max_length=14)
    destination = models.CharField(null=True, blank=False, max_length=100)
    is_emergency = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)

    class Meta:
        verbose_name_plural = "Booked Ambulances"
