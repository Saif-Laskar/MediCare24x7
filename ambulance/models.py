from statistics import mode
from unicodedata import category
from django.db import models
from accounts.models import PatientModel

# Create your models here.
CATEGORY=[
        ('Standard','Standard'),
        ('AC','AC'),
        ('Cardiac','Cardiac'),
        ('ICU','ICU'),
        ('Freezer','Freezer'),
    ]

DISTRICTS = [   # All Districts for ambulance city/location
        ('', 'Select a District'),
        ('Bagerhat', 'Bagerhat'),

        ('Bandarban', 'Bandarban'),

        ('Barguna', 'Barguna'),

        ('Barishal', 'Barishal'),

        ('Bhola', 'Bhola'),

        ('Bogura', 'Bogura'),

        ('Brahmanbaria', 'Brahmanbaria'),

        ('Chandpur', 'Chandpur'),

        ('Chapainawabganj', 'Chapainawabganj'),

        ('Chattogram', 'Chattogram'),

        ('Chuadanga', 'Chuadanga'),

        ('Cox’s Bazar', 'Cox’s Bazar'),

        ('Cumilla', 'Cumilla'),

        ('Dhaka', 'Dhaka'),

        ('Dinajpur', 'Dinajpur'),

        ('Faridpur', 'Faridpur'),

        ('Feni', 'Feni'),

        ('Gaibandha', 'Gaibandha'),

        ('Gazipur', 'Gazipur'),

        ('Gopalganj', 'Gopalganj'),

        ('Habiganj', 'Habiganj'),

        ('Jamalpur', 'Jamalpur'),

        ('Jashore', 'Jashore'),

        ('Jhalokati', 'Jhalokati'),

        ('Jhenaidah', 'Jhenaidah'),

        ('Joypurhat', 'Joypurhat'),

        ('Khagrachhari', 'Khagrachhari'),

        ('Khulna', 'Khulna'),

        ('Kishoreganj', 'Kishoreganj'),

        ('Kushtia', 'Kushtia'),

        ('Kurigram', 'Kurigram'),

        ('Lakshmipur', 'Lakshmipur'),

        ('Lalmonirhat', 'Lalmonirhat'),

        ('Madaripur', 'Madaripur'),

        ('Magura', 'Magura'),

        ('Manikganj', 'Manikganj'),

        ('Meherpur', 'Meherpur'),

        ('Moulvibazar', 'Moulvibazar'),

        ('Munshiganj', 'Munshiganj'),

        ('Mymensingh', 'Mymensingh'),

        ('Naogaon', 'Naogaon'),

        ('Narayanganj', 'Narayanganj'),

        ('Narail', 'Narail'),

        ('Narsingdi', 'Narsingdi'),

        ('Natore', 'Natore'),

        ('Netrokona', 'Netrokona'),

        ('Nilphamari', 'Nilphamari'),

        ('Noakhali', 'Noakhali'),

        ('Pabna', 'Pabna'),

        ('Panchagarh', 'Panchagarh'),

        ('Patuakhali', 'Patuakhali'),

        ('Pirojpur', 'Pirojpur'),

        ('Rajbari', 'Rajbari'),

        ('Rajshahi', 'Rajshahi'),

        ('Rangamati', 'Rangamati'),

        ('Rangpur', 'Rangpur'),

        ('Satkhira', 'Satkhira'),

        ('Shariatpur', 'Shariatpur'),

        ('Sherpur', 'Sherpur'),

        ('Sirajganj', 'Sirajganj'),

        ('Sunamganj', 'Sunamganj'),

        ('Sylhet', 'Sylhet'),

        ('Tangail', 'Tangail'),

        ('Thakurgaon', 'Thakurgaon')
    ]


class Ambulance(models.Model): # Ambulance model;
    "Here all the information is about a ambulance including its driver"
    
    
    vehicleNumber= models.CharField(max_length=20, unique=True) 
    city= models.CharField(max_length=20, choices= DISTRICTS ,null= False)
    category= models.CharField(max_length=20,choices= CATEGORY ,null= False)
    driverName= models.CharField(max_length=20, null=True, blank=True)
    driverContact= models.CharField(max_length=20, null=True, blank=True)
    driverEmail= models.EmailField(max_length=20, null=True, blank=True)
    driverAddress= models.CharField(max_length=20, null=True, blank=True)
    driverNID= models.CharField(max_length=20, null=True, blank=True, unique=True)
    driverLicense= models.CharField(max_length=20, null=True, blank=True,unique=True)
    driverBloodGroup= models.CharField(max_length=20, null=True, blank=True)
    driverGender= models.CharField(max_length=20, null=True, blank=True)
    driverImage= models.ImageField(null=True, blank=True)
    ambulanceImage= models.ImageField(null=True, blank=True)
    rentInterDivision = models.IntegerField(null=True, blank=True)
    rentIntraDivision = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'Ambulances'
        

class BookAmbulanceModel(models.Model):
    ambulance       = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    patient         = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    patientContact  = models.CharField(null=False, max_length=14)
    destination     = models.CharField(null= True, blank= False,max_length=100)
    is_emergency    = models.BooleanField(default=True)
    date            = models.DateField(null=True, blank=False)
    time            = models.TimeField(null= True, blank= False)


    class Meta:
        verbose_name_plural = 'Booked Ambulances'