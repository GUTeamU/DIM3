from django.conf.urls import *
from rct import views

urlpatterns = patterns('',
        url(r'^login/$', views.login, name='login'),
		url(r'^$', views.index, name='index'),

		)
