from django.conf.urls import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from chatroomApp.forms import *

urlpatterns = patterns('',

    url(r'^$', 'chatroomApp.views.home',name="home"),
    url(r'^add-message/(?P<id>\d+)$', 'chatroomApp.views.add_message', name="add"),
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name':'registration.html',
        'extra_context':{'login_form':AuthenticationForm(),'registration_form':RegistrationForm()}},
         name='login'),

    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
