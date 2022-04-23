from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from .forms import *
# Create your views here.


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

    is_complete = False # set is_complete to false
    prescription = None # set prescription to none
    if appointment.is_completed: # if the appointment is complete
        is_complete = True # set is_complete to true
        prescription = PrescriptionModel.objects.get(appointment=appointment) # get prescription from appointment

    context = { # create context to pass to frontend
        'appointment': appointment,
        'is_pending': is_pending,
        'is_complete': is_complete,
        'is_upcoming': is_upcoming,
        'prescription': prescription,
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
                             and appointment.is_complete == False]  # get all upcoming appointments
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