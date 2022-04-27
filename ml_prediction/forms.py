from django import forms
from .models import HeartAttackRiskModel


class HeartAttackRiskForm(forms.ModelForm):

    class Meta:
        model = HeartAttackRiskModel
        fields = '__all__'