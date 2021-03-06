from django.conf.urls import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from forms import *

urlpatterns = patterns('',

    url(r'^$', 'chatroomApp.views.home',name="home"),
    url(r'^room', 'chatroomApp.views.home'),

    url(r'^add-message$', 'chatroomApp.views.add_message', name="add_message"),
    url(r'^get-new-messages/(?P<id>\d+)$', 'chatroomApp.views.get_new_messages', name="get_new_messages"),
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name':'registration.html',
        'extra_context':{'login_form':AuthenticationForm(),'registration_form':RegistrationForm()}},
         name='login'),

    url(r'^register$', 'chatroomApp.views.register',name="register"),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),

)
