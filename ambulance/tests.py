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