from django.db import models

# Create your models here.

class Ambulance(models.Model): # Ambulance model;
    "Here all the information is about a ambulance including its driver"
    



    vehicleNumber= models.CharField(max_length=20, unique=True)
    city= models.CharField(max_length=20, null= False)
    category= models.CharField(max_length=20, null= False)
    driverName= models.CharField(max_length=20, null=True, blank=True)
    driverContact= models.CharField(max_length=20, null=True, blank=True)
    driverEmail= models.EmailField(max_length=20, null=True, blank=True)
    driverAddress= models.CharField(max_length=20, null=True, blank=True)
    driverNID= models.CharField(max_length=20, null=True, blank=True)
    driverLicense= models.CharField(max_length=20, null=True, blank=True)
    driverBloodGroup= models.CharField(max_length=20, null=True, blank=True)
    driverGender= models.CharField(max_length=20, null=True, blank=True)
    driverImage= models.ImageField(null=True, blank=True)
    ambulanceImage= models.ImageField(null=True, blank=True)
    rentInterDivision = models.IntegerField(null=True, blank=True)
    rentIntraDivision = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)


