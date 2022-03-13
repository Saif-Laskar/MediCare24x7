from .models import *
from django.forms import ModelForm



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

class AmbulanceForm(ModelForm):

    city = forms.ChoiceField(widget=forms.Select(choices=DISTRICTS))
    category = forms.ChoiceField(widget=forms.Select(choices=CATEGORY))
    class Meta:
        model = Ambulance
        fields = '__all__'