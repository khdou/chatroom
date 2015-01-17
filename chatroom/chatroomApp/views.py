from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext

# Needed to manually create HttpResponses or raise an Http404 exception
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Used to generate a one-time-use token to verify a user's email address
from django.contrib.auth.tokens import default_token_generator

# Used to send mail from within Django
from django.core.mail import send_mail

# Helper function to guess a MIME type from a file name
from mimetypes import guess_type

from models import *
from forms import *

# Create your views here.
@login_required
def home(request):
    context = {}
    return render(request,'templates/chat.html',context)

def add_message(request):
    context = {}
    return render(request,'templates/baseMessage.html',context)

@transaction.atomic
def register(request):
    context = {}

    context['login_form'] = AuthenticationForm()
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'templates/registration.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'templates/registration.html', context)
    # If we get here the form data was valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'],
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['username'])
    new_user.save()

    return render(request, 'templates/registered.html', context)