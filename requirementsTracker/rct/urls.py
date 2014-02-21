from django.conf.urls import *
from rct import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='/login/'))