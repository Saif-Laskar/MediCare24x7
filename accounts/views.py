from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .utils import *
from .forms import *


def home_view(request):  # The home page

    user = request.user  # Get the user
    if user.is_authenticated:
        if user.is_patient:
            return redirect('patient-dashboard')
        elif user.is_doctor:
            return redirect('doctor-dashboard')
        elif user.is_staff or user.is_admin:
            return redirect('staff-dashboard')

    return render(request, 'index.html')


def login_view(request):  # Log a user in

    if request.POST:  # If the form has been submitted...
        form = LoginForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            email = request.POST['email']  # Get the email
            password = request.POST['password']  # Get the password
            user = authenticate(email=email, password=password)  # Authenticate the user

            if user and user.is_doctor:  # If the user exists and is a doctor
                login(request, user)  # Log them in
                if request.GET.get('next'):  # If there is a next page
                    return redirect(request.GET.get('next'))  # Redirect to the next page
                return redirect('doctor-dashboard')  # Redirect to the doctor dashboard

            elif user and user.is_patient:  # If the user exists and is a patient
                login(request, user)  # Log them in
                if request.GET.get('next'):  # If there is a next page
                    return redirect(request.GET.get('next'))  # Redirect to the next page
                return redirect('home')  # Redirect to the patient dashboard
            
            elif user and user.is_staff: # If the user exists and is a staff
                login(request, user) # Log them in
                if request.GET.get('next'): # If there is a next page
                    return redirect(request.GET.get('next')) # Redirect to the next page
                return redirect('staff-dashboard') # Redirect to the staff dashboard


            else:  # If the user doesn't exist
                messages.error(request, 'Email or Password is incorrect.')  # Display an error message
                return redirect('login')  # Redirect to the login page
        else:  # The form is invalid
            return render(request, 'accounts/login.html', {'form': form})  # Render the login page

    form = LoginForm()  # An unbound form
    context = {  # Context to render the form
        'form': form  # The form
    }
    return render(request, 'accounts/login.html', context)  # Render the login page


def logout_view(request):  # Log a user out
    logout(request)  # Log the user out
    return redirect('home')  # Redirect to the home page



def patient_signup_view(request):  # The patient signup page
    if request.method == "POST":  # If the form has been submitted...
        patient_form = PatientRegistrationForm(request.POST)  # A form bound to the POST data
        if patient_form.is_valid():  # All validation rules pass
            print("Valid")
            patient_form.save()  # Save the form
            email = request.POST['email']  # Get the email
            password = request.POST['password1']  # Get the password
            user = authenticate(request, email=email, password=password)  # Authenticate the user
            user.is_patient = True
            user.save()  # Save the user
            print(user)
            PatientModel.objects.create(user=user)  # Create a patient model for the user
            login(request, user)  # Log the user in
            return redirect('patient-dashboard')  # Redirect to the patient dashboard
        else:  # The form is invalid
            print("Invalid")
            context = {  # Context to render the form
                'patient_form': patient_form  # The form
            }
            return render(request, 'accounts/signup.html', context)  # Render the signup page
    else:  # The form has not been submitted
        print("Unbound form")
        patient_form = PatientRegistrationForm()  # An unbound form

    context = {  # Context to render the form
        'patient_form': patient_form  # The form
    }
    return render(request, 'accounts/signup.html', context)  # Render the signup page

def patient_dashboard_view(request):
    user = request.user  # Get the user
    profile = PatientModel.objects.get(user=user)  # Get the patient's profile

    context = {  # Context to render the view
        'user': user,  # The user
        'profile': profile,  # The patient's profile
    }
    return render(request, 'accounts/patient-dashboard.html', context)

def staff_dashboard_view(request):

    user = request.user  # Get the user
    context={
        'user': user,
    }
    return render(request, 'accounts/staff-dashboard.html',context)

def patient_profile_edit_view(request):  # The patient profile edit page

    """
    this view is for editing the patient profile,
    from here the user can edit their on profile
    after editing the profile the user will be redirected to the patient profile page

    """



    user = request.user # Get the user
    profile = PatientModel.objects.get(user=user) # Get the patient's profile

    form = PatientEditProfileForm(instance=profile) # An unbound form

    if request.method == 'POST': # If the form has been submitted...
        form = PatientEditProfileForm(request.POST, request.FILES, instance= profile) # A form bound to the POST data

        if form.is_valid(): # check if the form is valid
            form.save() # save the form
            return redirect('patient-profile',user.id) # redirect to the patient profile page
        else: # the form is invalid
            return redirect('patient-profile') # redirect to the patient profile page

    context={   # Context to render the form
            'form': form,  # The form
            'profile': profile,  # The patient's profile
    }

    return render(request, 'accounts/edit-profile.html',context) # Render the edit profile page


def patient_profile_view(request,pk): # The patient profile page

    is_self= False # set the is_self variable to false

    user =UserModel.objects.get(id=pk) # get the user

    if request.user == user: # check if the user is the same as the user in the url
        is_self= True # set the is_self variable to true

    has_access=True #  set the has_access variable to true

    profile = PatientModel.objects.get(user=user) # get the patient's profile

    date_joined= calc_age(user.date_joined) # calculate the age of the user

    age = None
    if profile.date_of_birth: # check if the patient has a date of birth
        age= calc_age(profile.date_of_birth)    # calculate the age of the patient

    incomplete_profile = False      # set the incomplete_profile variable to false
    if not profile.gender or not profile.blood_group or not profile.date_of_birth or not \
            profile.phone or not profile.height or not profile.weight or not profile.address:
        incomplete_profile = True     # set the incomplete_profile variable to true

    context={  # Context to render the view
        'user':user, # the user
        'is_self':is_self, 
        'has_access':has_access,
        'profile':profile,
        'date_joined':date_joined,
        'age':age,


    }

    return render(request,"accounts/patient-profile.html",context)




def add_doctor_view(request):  # The doctor signup page
    """
    This view will render the doctor user adding page.
    :param request: The HTTP request

    This view renders a doctor registration form and then takes in an email and a password.
    if the email and password is authentic then it saves the user

    :return: renders the doctor signup page
    """
    if request.method == "POST":  # If the form has been submitted...
        doctor_form = DoctorRegistrationForm(request.POST)  # A form bound to the POST data
        if doctor_form.is_valid():  # All validation rules pass
            doctor_form.save()  # Save the form
            email = request.POST['email']  # Get the email
            password = request.POST['password1']  # Get the password
            user = authenticate(request, email=email, password=password)  # Authenticate the user
            user.is_doctor = True
            user.save()  # Save the user
            DoctorModel.objects.create(user=user)  # Create a doctor record for the user
            messages.success(request, 'Docotor Registration successfully registered!')
            return redirect('staff-dashboard')  # Redirect to the staff dashboard
        else:  # The form is invalid
            context = {  # Context to render the form
                'doctor_form': doctor_form  # The form
            }
            return render(request, 'accounts/add-doctor.html', context)  # Render the signup page
    else:  # The form has not been submitted
        doctor_form = DoctorRegistrationForm()  # An unbound form

    context = {  # Context to render the form
        'doctor_form': doctor_form  # The form
    }
    return render(request, 'accounts/add-doctor.html', context)  # Render the signup page

