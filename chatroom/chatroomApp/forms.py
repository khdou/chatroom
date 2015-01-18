from django import forms

from django.contrib.auth.models import User
from models import *
# Form used in the Registration page
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length = 12,
    							label='First Name')
    last_name = forms.CharField(max_length = 12,
    							label = 'Last Name')	
    username = forms.CharField(max_length = 30,
    							label='Email',
    							widget = forms.TextInput(attrs={'type':'email'}))
    password1 = forms.CharField(max_length = 20, 
                                label='Password', 
                                widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, 
                                label='Confirm password',  
                                widget = forms.PasswordInput())

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        last_name = cleaned_data.get('last_name')
        if User.objects.filter(last_name__exact=last_name):
            for user in User.objects.filter(last_name__exact=last_name):
                if user.first_name == cleaned_data.get('first_name'):
                    raise forms.ValidationError("Name already exists.")
        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Email is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username

