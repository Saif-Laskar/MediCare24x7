from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from health_records.forms import RecordForm
from health_records.models import HealthRecordModel
from user_control.models import UserModel, PatientModel

def health_record_home_view(request, pk):
    """
    This view is the main page for the user.
    It lists all of the records for the user.

    :param request: The request object
    :param pk: The primary key of the user
    :return: A rendered page

    This view will show all of the records for the user.
    """
    user = UserModel.objects.get(id=pk) # Get the user from the user_id
    patient = PatientModel.objects.get(user=user) # Get the patient from the user_id
    records = HealthRecordModel.objects.filter(patient=patient) # Get all of the records for the user

    paginator = Paginator(records, 5) # Show 5 records per page
    page = request.GET.get('page', 1) # Get the page number to display
    try:
        records = paginator.page(page) # Get the records for the page
    except PageNotAnInteger: # If page is not an integer, deliver first page.
        records = paginator.page(1)
    except EmptyPage: # If page is out of range, deliver last page of results
        records = paginator.page(paginator.num_pages)

    is_self = False # If the user is the user logged in, set this to true
    if request.user == user: # If the user is the user logged in, set this to true
        is_self = True # Set this to true

    context = { # Set the context for the view
        'records': records,
        'is_self': is_self
    }
    return render(request, "pages/health-records/record-home.html", context)
    