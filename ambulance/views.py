from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages



# Create your views here.
def add_ambulance_view(request):
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Ambulance successfully Added!')
            return redirect('staff-dashboard')
    else:
        form = AmbulanceForm()
    context={
        # 'task':"Post New", 
        'form': form,
    }
    return render(request, 'ambulance/add_ambulance.html', context)