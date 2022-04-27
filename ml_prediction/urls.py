from django.urls import URLPattern, path
from .views import *


urlpatterns=[
    path('Heart-Attack-Risk', heart_attack_risk_home_view, name='heart-risk'),
    
]