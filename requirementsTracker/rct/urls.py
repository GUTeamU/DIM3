from django.conf.urls import *
from rct import views

urlpatterns = patterns('',
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$',views.user_logout, name='logout'),
        url(r'^project/create/$', views.create_project, name='create_project'),
        url(r'^project/(?P<url>\w+)/$', views.view_project, name='project'),
        url(r'^project/(?P<url>\w+)/delete', views.delete_project, name='delete_project'),
        url(r'^project/(?P<url>\w+)/edit', views.edit_project, name='edit_project'),
        url(r'^project/(?P<url>\w+)/task/add$', views.add_task, name='add_task'),
        url(r'^project/(?P<projectURL>\w+)/(?P<task_id>\w+)/edit$', views.edit_task, name='edit_task'),
        url(r'^ajax/task/update$', views.update_task_completed, name='update_task'),
        url(r'^signup/$', views.signup, name='signup'),
	url(r'^$', views.index, name='index'),

		)
