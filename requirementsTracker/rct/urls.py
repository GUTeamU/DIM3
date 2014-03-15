from django.conf.urls import *
from rct import views

urlpatterns = patterns('',
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$',views.user_logout, name='logout'),
        url(r'^projectBoard/$', views.projectBoard, name='projectBoard'),
        url(r'^project/create/$', views.create_project, name='create_project'),
        url(r'^project/(?P<url>\w+)/$', views.view_project, name='project'),
        url(r'^project/(?P<url>\w+)/add_task/$', views.add_task, name='add_task'), ## not currently working.
        url(r'^signup/$', views.signup, name='signup'),
	url(r'^$', views.index, name='index'),

		)
