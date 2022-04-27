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
        (0,'Typical Angina'),
        (1,'Atypical Angina'),
        (2,'Non-anginal pain'),
        (3,'Asymptomatic')
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
    SLP=[
        (0,'0'),
        (1,'1'),
        (2,'2'),
    ]

    CAA=[
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    ]
    THAL=[
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3')
    ]


    age         = models.IntegerField(null= False, blank= False)
    sex         = models.IntegerField(null=False,blank=False, choices=GENDER) # gender
    cp          = models.IntegerField(null=False,blank=False, choices=CP) # chest paint type
    trtbps      = models.IntegerField(null=False,blank=False) # resting blood pressure (in mm Hg)
    chol        = models.IntegerField(null=False,blank=False) # cholestoral in mg/dl fetched via BMI sensor
    fbs         = models.IntegerField(null=False,blank=False, choices=FBS) # fasting blood sugar > 120 mg/dl
    restecg     = models.IntegerField(null=False,blank=False, choices= RESTECG) # resting electrocardiographic results
    thalachh     = models.IntegerField(null=False,blank=False) # maximum heart rate achieved
    exang       = models.IntegerField(null=False,blank=False, choices=EXANG) # exercise induced angina
    oldpeak     = models.FloatField(null=False,blank=False) # ST depression induced by exercise relative to rest
    slp         = models.IntegerField(null=False,blank=False,choices=SLP) # slope of the peak exercise ST segment
    caa         = models.IntegerField(null=False,blank=False,choices=CAA) # number of major vessels (0-3) colored by flourosopy
    thal        = models.IntegerField(null=False,blank=False, choices= THAL) # thalassemia
