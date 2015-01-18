from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm
from chatroomApp.forms import *

urlpatterns = patterns('',
    url(r'^chat/', include('chatroomApp.urls')),

    url(r'^$', 'chatroomApp.views.home',name="home"),

)
