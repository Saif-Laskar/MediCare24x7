from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json

# Create your tests here.

class TestAppointmentView(TestCase):

    def test_appointment_doctorList_view(self):
        response = self.client.get(reverse('doctorList'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2FdoctorList')
    
    def test_make_appointment_view(self):
        response = self.client.get(reverse('make-appointment', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fmake-appointment%2F1')
    
    def test_appointment_detail_view(self):
        response = self.client.get(reverse('appointment-detail', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdetail%2F1')

    def test_patient_all_appointments_view(self):
        response = self.client.get(reverse('patient-all-appointments'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fall-appointments')

    def test_doctor_all_appointments_view(self):
        response = self.client.get(reverse('doctor-all-appointments'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdoctor-all-appointments')
    
    def test_patient_update_appointment_view(self):
        response = self.client.get(reverse('patient-update-appointment', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fupdate-appointment%2F1')
    
    def test_doctor_update_appointment_view(self):
        response = self.client.get(reverse('doctor-update-appointment', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdoctor-update-appointment%2F1')
    
    def test_reject_appointment_view(self):
        response = self.client.get(reverse('reject-appointment', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Freject-appointment%2F1')

    def test_patient_delete_appointment_view(self):
        response = self.client.get(reverse('delete-appointment', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdelete-appointment%2F1')

    def test_write_prescription_view(self):
        response = self.client.get(reverse('write-prescription', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fwrite-prescription%2F1')
    
    def test_pdf_view(self):
        response = self.client.get(reverse('pdf-view', args=['1']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login?next=%2Fdownload-prescription%2F1')

    