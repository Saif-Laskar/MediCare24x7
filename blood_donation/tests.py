from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json


class TestingBloodDonation(TestCase):

    def test_blood_donation_home_view(self):
        response = self.client.get(reverse('blood-donation-home'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fblood-donation-home')

    def test_post_blood_request_view(self):
        response = self.client.get(reverse('blood-donation-post-request'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpost-request')

    def test_blood_request_detail_view(self):
        response = self.client.get(reverse('blood-donation-request-detail', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frequest-detail%2F1')

    def test_update_blood_request_view(self):
        response = self.client.get(reverse('blood-donation-update-request', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fupdate-request%2F1')

    def test_delete_blood_request_view(self):
        response = self.client.get(reverse('blood-donation-delete-request', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdelete-request%2F1')

    def test_users_requests_view(self):
        response = self.client.get(reverse('users-requests', args=[1]))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Frequests%2F1')