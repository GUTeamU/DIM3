from django.conf.urls import *
from rct import views

urlpatterns = patterns('',
        url(r'^login/$', views.login, name='login'),
        url(r'^projectBoard/$', views.projectBoard, name='projectBoard'),
        url(r'^project/create/$', views.create_project, name='create_project'),
        url(r'^project/(?P<url>\w+)/$', views.view_project, name='project'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^loginManual/$', views.loginManual, name='loginManual'),
		url(r'^$', views.index, name='index'),
		
        #url(r'^logout/$',views.logout, name='logout'),
		#url(r'^project/(?P<url>\w+)/add_task/$',views.add_task, name='add_task'), #new addition
        #url(r'^project/(?P<url>\w+)/(?P<task_url>\w+)/$',views.task, name='task'), # also new
		)
