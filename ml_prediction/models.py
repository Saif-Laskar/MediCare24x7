from django.db import models

# Create your models here.

class HeartAttackRiskModel(models.Model):
    """
    This class represents the Heart Attack Risk Model.
    This model contains these attributes:
    - age: The age of the patient
    -"""
    GENDER=[
        (1,'Male'),
        (0,'Female')
    ]

    CP=[
        (1,'Normal'),
        (2,'Medium'),
        (3,'Extreme')
    ]

    FBS=[
        (0,'0'),
        (1,'1')
    ]

    RESTECG =[
        (0,'0'),
        (1,'1'),
    ]

    EXANG =[
        (1,'YES'),
        (0,'NO')
    ]


    age         = models.IntegerField(null= False, blank= False),
    sex         = models.IntegerField(null=False,blank=False, choices=GENDER) # gender
    CP          = models.IntegerField(null=False,blank=False, choices=CP) # chest paint type
    trtbps      = models.IntegerField(null=False,blank=False) # resting blood pressure (in mm Hg)
    chol        = models.IntegerField(null=False,blank=False) # cholestoral in mg/dl fetched via BMI sensor
    fbs         = models.IntegerField(null=False,blank=False, choices=FBS) # fasting blood sugar > 120 mg/dl
    restecg     = models.IntegerField(null=False,blank=False, choices= RESTECG) # resting electrocardiographic results
    thalachh     = models.IntegerField(null=False,blank=False) # maximum heart rate achieved
    exang       = models.IntegerField(null=False,blank=False, choices=EXANG) # exercise induced angina
    oldpeak     = models.IntegerField(null=False,blank=False) # ST depression induced by exercise relative to rest

