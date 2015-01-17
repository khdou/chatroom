from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^chat/', include('chatroomApp.urls')),
    url(r'^$', 'chatroomApp.views.home'),

)
