from django.urls import path

from .views import *
urlpatterns = [
    path('<str:pk>', health_record_home_view, name='health-record-home'),
    
]
