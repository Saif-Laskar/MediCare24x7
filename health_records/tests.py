from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json


class TestHealthRecordsViews(TestCase):

    def test_health_record_home_view(self):
        response = self.client.get(reverse('health-record-home', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2F1')

    def test_health_record_create_view(self):
        response = self.client.get(reverse('health-record-create'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frecord%2Fnew%2F')

    def test_health_record_detail_view(self):
        response = self.client.get(reverse('health-record-post-detail', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frecord%2F1%2F')

    def test_health_record_update_view(self):
        response = self.client.get(reverse('health-record-post-update', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frecord%2Fupdate%2F1%2F')

    def test_health_record_delete_view(self):
        response = self.client.get(reverse('health-record-post-delete', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frecord%2Fdelete%2F1%2F')