from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blood_donation.forms import BloodRequestForm
from blood_donation.models import BloodRequestModel
from accounts.models import UserModel

from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url="login")
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


@login_required(login_url="login")
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

@login_required(login_url="login")
def blood_request_detail_view(request, pk):  # blood request detail page
    """
    This view will show the details of a specific blood request.
    parms: request, user id
    returns: render of the page

    This view will show the details of a specific blood request, and functionality to activate or deactivate the request.

    It will also show a map of the address where the blood is needed.
    """
    post = BloodRequestModel.objects.get(id=pk) # get the blood request
    print(post.is_active)

    my_post = False # set to false to show that this is not my post
    if request.user.is_authenticated and post.user == request.user: # if the user is logged in and the user who posted the request is the logged in user
        my_post = True # set to true to show that this is my post

    location_link = "https://maps.google.com/maps?width=100%25&amp;height=450&amp;hl=en&amp;q=" # create a link to the google maps page with the latitude and longitude of the request

    if post.location is not None: # if the location is not null
        locations = post.location.split(' ') # split the location into latitude and longitude
        location_link = "https://maps.google.com/maps?width=100%25&amp;height=450&amp;hl=en&amp;q=" 

        for location in locations:
            location_link += location + "%20"

        location_link += "&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed" #

    if request.GET.get('disable_req'): # if the user has clicked the disable request button
        post.is_active = False # set the is_active to false
        post.save() # save the post
        return redirect('blood-donation-request-detail', post.id) # redirect to the request detail page

    if request.GET.get('activate_req'): # if the user has clicked the activate request button
        post.is_active = True # set the is_active to true
        post.save() # save the post
        return redirect('blood-donation-request-detail', post.id) # redirect to the request detail page

    context = { # context to pass to template
        'post': post,
        'my_post': my_post,
        'location_link': location_link
    }
    return render(request,'blood_donation/blood-donation-request-details.html',context)


@login_required(login_url="login")
def update_blood_request_view(request, pk):  # update blood request
    """
    This view will show the details of a specific blood request.
    parms: request, user id
    returns: render of the page

    This view will show a form for the user to update a specific blood request.
    """
    task = "Update"
    post = BloodRequestModel.objects.get(id=pk) # get the blood request
    form = BloodRequestForm(instance=post) # create a blank form
    if request.method == 'POST': # if the form has been submitted
        form = BloodRequestForm(request.POST, instance=post) # create a form from the submitted data
        if form.is_valid(): # check if the form is valid
            form.save() # save the form
            return redirect('blood-donation-request-detail', post.id) # redirect to the request detail page
        else: # if the form is not valid
            return redirect('blood-donation-update-request', post.id) # redirect to the request update page
    context = {
        'task': task,
        'post': post,
        'form': form,
    }
    return render(request,'blood_donation/blood-donation-create-update-request.html',context)


@login_required(login_url="login")
def delete_blood_request_view(request, pk):  # delete blood request
    """
    This view will delete a specific blood request.
    parms: request, user id
    returns: redirect to the request list page

    This view will delete a specific blood request.
    """
    post = BloodRequestModel.objects.get(id=pk) # get the blood request
    if request.method == 'POST': # if the form has been submitted
        post.delete() # delete the blood request
        return redirect('users-requests', post.user.id) # redirect to the user's requests page

    context = {
        'post': post,
    }
    return render(request,'blood_donation/blood-donation-request-delete.html',context)


@login_required(login_url="login")
def users_requests_view(request, pk):  # users requests page
    """
    This view will show all the blood requests for a user.
    parms: request, user id
    returns: render of the page

    This view will show all the blood requests for a specific user.
    """
    user = UserModel.objects.get(id=pk) # get the user
    blood_requests = BloodRequestModel.objects.filter(user=user).order_by('-posted_on') # get all the blood requests of the user by order of posted date on descending order

    paginator = Paginator(blood_requests, 16) # show 16 requests per page
    page = request.GET.get('page', 1) # get the page number

    try:
        blood_requests = paginator.page(page) # get the requested page
    except PageNotAnInteger: # if page is not an integer, deliver first page
        blood_requests = paginator.page(1)
    except EmptyPage: # if page is out of range, deliver last page of results
        blood_requests = paginator.page(paginator.num_pages)

    context = {
        'user': user,
        'blood_requests': blood_requests,
    }
    return render(request, 'blood_donation/user-requests.html', context)

