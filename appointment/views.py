from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
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