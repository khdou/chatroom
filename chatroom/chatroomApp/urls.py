from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',

    url(r'^chat/', include('chatroomApp.urls')),
    url(r'^add_message/', 'chatroomApp.views.add_message',name="add"),
    url(r'^$', 'chatroomApp.views.home',name="home"),
    url(r'^login$', 'django.contrib.auth.views.login', \
        {'template_name':'templates/registration.html', \
        'extra_context':{'login_form':AuthenticationForm(),'form':RegistrationForm()}}, \
         name='login'),

    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),

)
