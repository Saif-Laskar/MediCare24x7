from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blood_donation.forms import BloodRequestForm
from blood_donation.models import BloodRequestModel
from accounts.models import UserModel


# Create your views here.
def blood_donation_home_view(request):  # blood donation home page
    """
    This view is the main page for the blood donation app.
    parms: request

    This view renders the home page for the blood donation app along with the active blood requests.

    returns: render of the page
    """

    blood_requests = BloodRequestModel.objects.filter(is_active=True).order_by('-posted_on') # get all active blood requests by date posted on descending order

    paginator = Paginator(blood_requests, 16) # Show 16 requests per page
    page = request.GET.get('page', 1) # get page number from url
    try: 
        blood_requests = paginator.page(page) # get the requested page
    except PageNotAnInteger: # if page is not an integer, deliver first page
        blood_requests = paginator.page(1)
    except EmptyPage: # if page is out of range, deliver last page of results
        blood_requests = paginator.page(paginator.num_pages)

    context = { # context to pass to template
        'blood_requests': blood_requests,
    }
    return render(request, 'blood_donation/blood-donation-home.html' ,context) # render the page to see all the requests


def post_blood_request_view(request):  # post blood request
    """
    This view is the main page for the blood donation app.
    parms: request

    This view renders a form for the user to post a request for blood.

    returns: render of the page    
    """
    task = "Post New" 
    form = BloodRequestForm() # create a blank form

    if request.method == 'POST': # if the form has been submitted
        form = BloodRequestForm(request.POST) # create a form from the submitted data
        if form.is_valid(): # check if the form is valid
            blood_request = form.save(commit=False) # create a new blood request
            blood_request.user = request.user # set the user to the current logged in user
            blood_request.save() # save the blood request
            return redirect('blood-donation-home') # redirect to the home page

    context = { # context to pass to template
        'task': task,
        'form': form,
    }
    return render(request,'blood_donation/blood-donation-create-update-request.html',context)

