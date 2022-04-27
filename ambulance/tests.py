from django.test import TestCase, Client
from django.urls import reverse
from ambulance.models import *
import json
# Create your tests here.

class TestAmbulanceView(TestCase):

    def test_add_ambulance_view(self):
        response = self.client.get(reverse('add-ambulance'))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fadd-ambulance%2F')

    def test_edit_ambulance_view(self):
        response = self.client.get(reverse('edit-ambulance-details', args=['1']))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fambulance%2Fedit-ambulance-details%2F1')

    def test_staff_abmulance_view(self):
        response = self.client.get(reverse('staff-all-ambulance'))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fstaff-all-ambulance%2F')

    def test_ambulance_detail_view(self):
        response = self.client.get(reverse('ambulance-details', args=['1']))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fambulance%2Fambulance-details%2F1')

    def test_patient_available_abmulance_view(self):
        response = self.client.get(reverse('patient-available-abmulance'))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpatient-available-abmulance%2F')
    
    def test_ambulance_booking_view(self):
        response = self.client.get(reverse('ambulance-booking',args=['1']))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fambulance-booking%2F1')

    def test_confirm_ambulance_booking_view(self):
        response = self.client.get(reverse('cinfirm-ambulance-booking',args=['1']))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fcinfirm-ambulance-booking%2F1')
    
    def test_staff_available_ambulance_view(self):
        response = self.client.get(reverse('staff-available-ambulance'))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fstaff-available-ambulance%2F')

    def test_staff_booked_ambulance_view(self):
        response = self.client.get(reverse('staff-booked-ambulance'))
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response, '/accounts/login?next=%2Fstaff-booked-ambulance%2F')
