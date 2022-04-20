from asyncio.windows_events import NULL
from webbrowser import get
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages



# Create your views here.
def add_ambulance_view(request):    # add-ambulance view, this view is for staff to add ambulance
    if request.method == 'POST':    # if the request is a post request
        form = AmbulanceForm(request.POST) # create a form object with the data from the request
        if form.is_valid(): # if the form is valid
            form.save() # save the form, if valid
            messages.success(request, 'New Ambulance successfully Added!')  # display success message, if the ambulance is successfully added
            return redirect('staff-dashboard')  # redirect to staff-dashboard view, after a successfull ambulance addition
    else: # if the request is not a post request
        form = AmbulanceForm()  # create a form object
    context={
        # 'task':"Post New", 
        'form': form, # pass the form object to the context
    }
    return render(request, 'ambulance/add_ambulance.html', context)     # render the add_ambulance.html template with the context




def staff_abmulance_view(request):  # staff-all-ambulance view, this view is for staff to view all ambulances
    ambulances = Ambulance.objects.all()    # get all ambulances from the database
    context = { 
        'ambulances': ambulances, # pass the ambulances to the context
    }
    return render(request, 'ambulance/staff-all-ambulance.html', context)   # render the staff-all-ambulance.html template with the context




def ambulance_detail_view(request, pk):
    ambulance= Ambulance.objects.get(id=pk)
    is_patient= False
    is_doctor = False
    is_staff  = False
    has_city  = False
    user=request.user
    if user.is_patient:
        is_patient=True
    elif user.is_doctor:
        is_doctor=True
    else:
        is_staff= True



    if ambulance.city:
        has_city = True
        location_link = "https://maps.google.com/maps?width=100%25&amp;height=450&amp;hl=en&amp;q=" + ambulance.city + "&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed" 
    
    context={
        "ambulance"  : ambulance,
        "is_patient" : is_patient,
        "is_doctor"  : is_doctor,
        "is_staff"   :is_staff,
        "has_city"   : has_city,
        "location_link" :location_link,
    }

    return render(request,'ambulance/ambulance-details.html',context)

