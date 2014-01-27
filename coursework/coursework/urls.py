from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coursework.views.home', name='home'),
    # url(r'^coursework/', include('coursework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^todo/', include('ToDo.urls')),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^google/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
	url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
)
