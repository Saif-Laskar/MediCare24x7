from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *


def home_view(request):  # The home page
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
            return redirect('home')  # Redirect to the patient dashboard
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
