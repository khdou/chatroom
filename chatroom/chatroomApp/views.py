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
from datetime import datetime

# Create your views here.
@login_required
def home(request):
    context = {}
    # Sorts all messages by date
    context['messages'] = Message.objects.all().order_by('date')
    context['message_form'] = MessageForm()
    return render(request,'chat.html',context)

@login_required
@transaction.atomic
def add_message(request):
    context = {}
    if request.GET:
        return redirect(request.META.get("HTTP_REFERER"))
    user = request.user
    new_message = Message(owner=user,date=datetime.now())

    form = MessageForm(request.POST,instance=new_message)
    if not form.is_valid():
        return redirect(reverse('home'))

    form.save()

    return redirect(reverse('home'))

@transaction.atomic
def register(request):
    context = {}

    context['login_form'] = AuthenticationForm()
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['registration_form'] = RegistrationForm()
        return render(request, 'registration.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    registration_form = RegistrationForm(request.POST)
    context['registration_form'] = registration_form

    # Validates the form.
    if not registration_form.is_valid():
        return render(request, 'registration.html', context)
    # If we get here the form data was valid.  Register and login the user.
    new_user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                        first_name=registration_form.cleaned_data['first_name'],
                                        last_name=registration_form.cleaned_data['last_name'],
                                        password=registration_form.cleaned_data['password1'],
                                        email=registration_form.cleaned_data['username'])
    new_user.save()
    context['registered'] = "You have successfully registered!"
    return render(request, 'registration.html', context)