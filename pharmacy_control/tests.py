from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json

class TestPharmancyViews(TestCase):

    def test_pharmacy_home_view(self):
        response = self.client.get(reverse('pharmacy-home'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2F')

    def test_pharmacy_medicine_view(self):
        response = self.client.get(reverse('medicine-details', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2Fmedicine%2F1')

    def test_pharmacy_cart_view(self):
        response = self.client.get(reverse('pharmacy-cart'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2Fcart')

    
    def test_proceed_order(self):
        response = self.client.get(reverse('proceed-order'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2Fproceed-order')

    def test_confirm_order(self):
        response = self.client.get(reverse('confirm-order', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2Fconfirm-order%2F1')

    def test_order_details(self):
        response = self.client.get(reverse('order-details', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fpharmacy%2Forder-details%2F1')