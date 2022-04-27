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
    return render(request, "health-records/record-home.html", context)

def health_record_create_view(request):
    """
    A view to create a new record.

    :param request: The request object
    :return: A rendered page

    This view will show a form to create a new record.    
    """
    task = "Create New"
    form = RecordForm() # An unbound form
    patient = PatientModel.objects.get(user=request.user) # Get the patient from the user_id

    if request.method == 'POST': # If the form has been submitted...
        form = RecordForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            record = form.save(commit=False) # Create a new record
            record.patient = patient # Set the patient to the patient logged in
            record.save() # Save the record
            return redirect('health-record-home', request.user.id) # Redirect after POST

    context = { # Set the context for the view
        'task': task,
        'form': form,
    }
    return render(request, "health-records/record-create-update.html", context) # renders a page to create a new record

def health_record_detail_view(request, pk):
    """
    This view is the detail page for a record.
    It lists all of the details for the record.

    :param request: The request object
    :param pk: The primary key of the record
    :return: A rendered page
    
    """
    record = HealthRecordModel.objects.get(id=pk) # Get the record from the id

    my_record = False # If the user is the user logged in, set this to true
    if request.user == record.patient.user: # If the user is the user logged in, set this to true
        my_record = True # Set this to true

    context = { # Set the context for the view
        'record': record,
        'my_record': my_record,
    }
    return render(request, "health-records/record-details.html", context) # renders a page to show the record details

def health_record_update_view(request, pk):
    """
    This view is the detail page for a record.
    It populates the form with all of the details for the record.

    :param request: The request object
    :param pk: The primary key of the record
    :return: A rendered page

    This view will show a form to update a record.
    """
    task = "Update"
    record = HealthRecordModel.objects.get(id=pk) # Get the record from the id

    form = RecordForm(instance=record) # An unbound form
    if request.method == 'POST': # If the form has been submitted...
        form = RecordForm(request.POST, instance=record) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save() # Save the record
            return redirect('health-record-post-detail', record.id) # Redirect after POST
    context = { # Set the context for the view
        'record': record,
        'task': task,
        'form': form,
    }
    return render(request, "health-records/record-create-update.html", context) # renders a page to update a record