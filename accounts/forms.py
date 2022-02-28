from django import forms
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.forms import ModelForm

from .models import *


class LoginForm(forms.Form):  # LoginForm
    """
    This form is used to login a user.

    This form displays an email, and a password field.
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))  # email
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))  # password

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def clean(self):  # clean
        if self.is_valid():
            email = self.cleaned_data.get('email')  # get cleaned email
            password = self.cleaned_data.get('password')  # get cleaned password
            if not authenticate(email=email, password=password):  # if email and password are not valid
                raise forms.ValidationError("Invalid Username or Password")  # raise error


class DoctorRegistrationForm(UserCreationForm):
    """
    This form is used to register a doctor.

    This form displays an email, a name, a password, and a confirm password field.
    """
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address',
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text='Password must contain at least 8 character including numeric values',
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text='Re-type Password',
    )
    # check = forms.BooleanField(required=True)

    class Meta:
        model = UserModel
        fields = ("name", "email", "password1", "password2")


class PatientRegistrationForm(UserCreationForm):
    """
    This form is used to register a patient.

    This form displays an email, a name, a password, and a confirm password field.
    """
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address',
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text='Password must contain at least 8 character including numeric values',
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text='Re-type Password',
    )

    class Meta:
        model = UserModel
        fields = ("name", "email", "password1", "password2")


class PatientEditProfileForm(ModelForm):
    # image = forms.ImageField(
    #     required=False,
    #     error_messages={'invalid': "Image files only"},
    #     widget=forms.FileInput,
    # ) 
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'})) 
    last_donation = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientModel  
        fields = '__all__' 
        exclude = ['user'] 