from django.urls import path

from .views import *
urlpatterns = [
    path('<str:pk>', health_record_home_view, name='health-record-home'),
    path('record/new/', health_record_create_view, name='health-record-create'),
]
