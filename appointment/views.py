from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from accounts.models import *
from .forms import *


@login_required(login_url='login')
def appointment_doctorList_view(request):
    doctors = DoctorModel.objects.all()
    specializations = [sp[0] for sp in  DoctorModel.SpecializationModel]
    doctorsmodel = DoctorModel.objects.all()
    doctors =[doctor for doctor in doctorsmodel if doctor.specialization is not None]
    context={
        'doctors':doctors,
        'specializations':specializations,
    }
    return render(request, 'appointment/doctorList.html',context)


@login_required(login_url='login')
def make_appointment_view(request,pk):
    """
        This view allows registered patitient type user
        to make appointment request to doctors,

    """

    doctor = DoctorModel.objects.get(user=UserModel.objects.get(id=pk)) # get doctor object
    patient = PatientModel.objects.get(user=request.user) # get patient object

    form = PatientAppointmentForm() # empty form
    if request.method == 'POST': # if request method is post
        form = PatientAppointmentForm(request.POST) # get form object
        if form.is_valid(): # if form is valid
            print(form.cleaned_data['date'])
            if form.cleaned_data['date'] < datetime.date.today(): # if the date is less than today's date
                messages.error(request, 'Date cannot be less than today\'s date') # display error message
                
                context={
                    'form':form,
                    'doctor':doctor,
                    'patient':patient,
                }

                return redirect('make-appointment',pk) # redirect to make-appointment view
            
            count= AppointmentModel.objects.filter(doctor=doctor,date=form.cleaned_data['date']).count() # get the count of appointments for the doctor on the same date
            
            if  count== 20:
                messages.error(request, 'Appointment Limit of This Doctor is Full on this date, Please Try Another Date') # display error message
                context={
                    'form':form,
                    'doctor':doctor,
                    'patient':patient,
                }
                return redirect('make-appointment',pk) # redirect to make-appointment view

            appointment = form.save(commit=False) # Create new appointment object
            appointment.patient = patient  # Set current user, who is patient, as patient of new appointment
            appointment.doctor = doctor  # Set the doctor for the new appointment
            appointment.save() # Save the new appointment

            return redirect('appointment-detail', appointment.id) # redirect to appointment detail page after new appointment is created

        else:
            context={
                'form':form,
                'doctor':doctor,
                'patient':patient,
            }
        return render(request, 'appointment/make-appointment.html',context)
    
    context={
        'form':form,
        'doctor':doctor,
        'patient':patient,
    }
    return render(request, 'appointment/make-appointment.html',context)



@login_required(login_url='login')
def appointment_detail_view(request,pk):
    """
        This view allows registered doctor and patient type user
        to view appointment details,

    """
    appointment = AppointmentModel.objects.get(id=pk)
    print(appointment)
    is_pending = False

    if (appointment.is_accepted == False and
        appointment.is_canceled == False and
        appointment.is_completed == False): # if the appointment is not accepted, canceled, or complete
        is_pending = True # set is_pending to true

    is_upcoming = False # set is_upcoming to false
    if (appointment.is_accepted == True and
        appointment.is_canceled == False and
        appointment.is_completed == False): # if the appointment is accepted but not complete
        is_upcoming = True # set is_upcoming to true

    is_completed = False # set is_complete to false
    prescriptions = None # set prescription to none
    if appointment.is_completed: # if the appointment is complete
        is_completed = True # set is_complete to true
        prescriptions = PrescriptionModel.objects.filter(appointment=appointment) # get prescription from appointment
        
    context = { # create context to pass to frontend
        'appointment': appointment,
        'is_pending': is_pending,
        'is_completed': is_completed,
        'is_upcoming': is_upcoming,
        'prescriptions': prescriptions,
    }
    return render(request, 'appointment/appointment-detail.html', context) # render the page


@login_required(login_url='login')
def patient_all_appointments_view(request):
    """
        This view allows registered patient type user
        to view all appointments they have made,

    """
    user = request.user  # get current user from request
    patient = PatientModel.objects.get(user=user)  # get current patient from user
    appointments = AppointmentModel.objects.filter(patient=patient)  # get all appointments for current patient
    pending_appointments = [appointment for appointment in appointments
                            if appointment.is_accepted == False
                            and appointment.is_canceled == False
                            and appointment.is_completed == False]  # get all pending appointments
    upcoming_appointments = [appointment for appointment in appointments
                             if appointment.is_accepted == True
                             and appointment.is_canceled == False
                             and appointment.is_completed == False]  # get all upcoming appointments
    rejected_appointments = [appointment for appointment in appointments
                             if appointment.is_accepted == False
                             and appointment.is_canceled == True
                             and appointment.is_completed == False]  # get all rejected appointments
    completed_appointments = [appointment for appointment in appointments
                              if appointment.is_accepted == True
                              and appointment.is_canceled == False
                              and appointment.is_completed == True]  # get all completed appointments

    context = {  # create context to pass to frontend
        'pending_appointments': pending_appointments,
        'upcoming_appointments': upcoming_appointments,
        'rejected_appointments': rejected_appointments,
        'completed_appointments': completed_appointments,
    }
    return render(request, 'appointment/patient-all-appointment.html', context)  # render the page

@login_required(login_url='login')
def doctor_all_appointments_view(request):
    """
        This view allows registered doctor type user
        to view all appointments they have made,

    """
    user = request.user  # get current user from request
    doctor = DoctorModel.objects.get(user=user)  # get current doctor from user
    appointments = AppointmentModel.objects.filter(doctor=doctor)  # get all appointments for current doctor
    pending_appointments = [appointment for appointment in appointments if appointment.is_canceled == False and appointment.is_completed == False]
    upcoming_appointments = [appointment for appointment in appointments if appointment.is_accepted == True and appointment.is_canceled == False and appointment.is_completed == False]
    completed_appointments = [appointment for appointment in appointments if appointment.is_accepted == True and appointment.is_canceled == False and appointment.is_completed == True]

    context = {  # create context to pass to frontend
        'pending_appointments': pending_appointments,
        'upcoming_appointments': upcoming_appointments,
        'completed_appointments': completed_appointments,
    }

    return render(request, 'appointment/doctor-all-appointment.html', context)  # render the page

@login_required(login_url='login')
def patient_update_appointment_view(request,pk):
    """
        This view allows registered patient type user
        to update an appointment he has made,

    """
    appointment = AppointmentModel.objects.get(id=pk)
    form = PatientAppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            if form.cleaned_data['date'] < datetime.date.today(): # if the date is less than today's date
                messages.error(request, 'Date cannot be less than today\'s date') # display error message
                return redirect('patient-update-appointment', appointment.id) # redirect to update appointment page
            count= AppointmentModel.objects.filter(doctor=appointment.doctor,date=form.cleaned_data['date']).count() # get the count of appointments for the doctor on the same date
            if  count==20:
                messages.error(request, 'Appointment Limit of This Doctor is Full on this date, Please Try Another Date') # display error message
                return redirect('patient-update-appointment', appointment.id) # redirect to update appointment page
            form.save()
            return redirect('appointment-detail', appointment.id)
    
    context={
        'form':form,
        'appointment':appointment,
    }
    return render(request, 'appointment/patient-update-appointment.html',context)


@login_required(login_url='login')
def doctor_update_appointment_view(request,pk):
    """
        This view allows registered doctor type user
        to update an appointment he has made,

    """
    appointment = AppointmentModel.objects.get(id=pk)
    form = DoctorAppointmentForm(instance=appointment)

    if request.method == 'POST':

        form = DoctorAppointmentForm(request.POST, instance=appointment)
        
        if form.is_valid():
        
            if form.cleaned_data['date'] < datetime.date.today(): # if the date is less than today's date
                messages.error(request, 'Date cannot be less than today\'s date') # display error message
                return redirect('doctor-update-appointment', appointment.id) # redirect to update appointment page
        
            appointment= form.save()
            appointment.is_accepted=True
            appointment.save()
        
            return redirect('appointment-detail', appointment.id)
    
    context={
        'form':form,
        'appointment':appointment,
    }
    return render(request, 'appointment/doctor-update-appointment.html',context)


@login_required(login_url='login')
def reject_appointment_view(request,pk):
    """
        This view allows registered doctor type user
        to reject an appointment he has made,

    """
    appointment = AppointmentModel.objects.get(id=pk)
    appointment.is_accepted=False
    appointment.is_canceled=True
    appointment.save()
    return redirect('doctor-all-appointments')


@login_required(login_url='login')
def patient_delete_appointment_view(request,pk):
    """
        This view allows registered patient type user
        to delete an appointment he has made,
    """
    appointment = AppointmentModel.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('patient-all-appointments')
    context={
        'appointment':appointment,
    }
    return render(request, 'appointment/delete-appointment.html',context)


@login_required(login_url='login')  # redirects to login if user is not logged in
def write_prescription_view(request, pk):
    """
    This view is for a doctor to write a prescription.

    :param request: the HttpRequest
    :param pk: the primary key of the appointment to update
    :return: a rendered page

    This view is only accessible to logged in users who are doctors.
    Doctors will be able to write a prescription from this page.
    """
    appointment = AppointmentModel.objects.get(id=pk) # get current appointment from id

    form = PrescriptionForm() # create a new form
    if request.method == 'POST': # If the form has been submitted...
        form = PrescriptionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print("valid")
            prescription = form.save(commit=False) # create a new prescription
            prescription.appointment = appointment # add appointment to prescription
            prescription.save() # save prescription

            appointment.is_completed = True # set appointment to complete
            appointment.save() # save appointment
            return redirect('appointment-detail', appointment.id) # redirect to appointment details page
        else: # the form is not valid
            context = { # create context to pass to frontend
                'appointment': appointment,
                'form': form,
            }
            return render(request, 'appointment/appointment-detail.html', context) # render the page

    context = {
        'appointment': appointment,
        'form': form,
    }
    return render(request, 'appointment/write-prescription.html', context)
