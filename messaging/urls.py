from django.conf.urls import patterns, url
from messaging import views

urlpatterns = patterns('',
        url(r'^messaging/messaging$', views.messages, name='messages'),
        url(r'^messaging/messaging/$', views.new_message, name='new_message'),
        )