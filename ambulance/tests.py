from django.test import TestCase, Client
from django.urls import reverse
from ambulance.models import *
import json
# Create your tests here.

class TestAmbulanceView(TestCase):

    def test_add_ambulance_view(self):
        response = self.client.get(reverse('add-ambulance'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'ambulance/add_ambulance.html')