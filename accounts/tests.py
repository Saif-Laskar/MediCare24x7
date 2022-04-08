from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import UserModel, PatientModel, DoctorModel
import json
# Create your tests here.

class TestViews(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_add_doctor_view_view(self):
        response = self.client.get(reverse('add-doctor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/add-doctor.html')

    def test_patient_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_doctor_dashboard(self):
        response = self.client.get(reverse('doctor-dashboard'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/doctor-dashboard')


    def test_patient_dashboard(self):
        response = self.client.get(reverse('patient-dashboard'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/patient-dashboard')

    def test_doctor_profile_view(self):
        response = self.client.get(reverse('doctor-profile', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/doctor-profile/1')

    def test_patient_profile_view(self):
        response = self.client.get(reverse('patient-profile', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/patient-profile/1')

    def test_doctor_edit_profile(self):
        response = self.client.get(reverse('doctor-edit-profile'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/doctor-edit-profile')

    def test_patient_edit_profile(self):
        response = self.client.get(reverse('patient-edit-profile'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/patient-edit-profile')
    
    def test_staff_dashboard(self):
        response = self.client.get(reverse('staff-dashboard'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=/accounts/staff-dashboard')