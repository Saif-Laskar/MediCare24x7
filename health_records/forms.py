from django import forms
from .models import HealthRecordModel


class RecordForm(forms.ModelForm):
    """
    This form is used to create a new health record for a patient.

    This form consists of two fields.
     - title: The title of the health record.
     - content: The content of the health record.
    """
    class Meta:
        model = HealthRecordModel
        fields = ['title', 'content']
