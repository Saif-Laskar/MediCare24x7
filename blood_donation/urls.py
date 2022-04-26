from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path('blood-donation-home', views.blood_donation_home_view, name='blood-donation-home'), # path for home page
]
