from django.db import models

from accounts.models import PatientModel


class HealthRecordModel(models.Model):
    """
    This class represents the Health Record Model.
    This model contains these attributes:
    - patient: ForeignKey to the PatientModel
    - title: The title of the health record
    - content: The content of the health record
    - posted_on: The date the health record was posted
    """
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
