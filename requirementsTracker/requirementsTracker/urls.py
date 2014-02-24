from django.conf.urls import *
from django.http import *
from django.views.generic.base import RedirectView
# from django.contrib import admin

# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('', include('social_auth.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^rct/', include('rct.urls')),

    # url(r'^$', 'requirementsTracker.views.home', name='home'),
    # url(r'^requirementsTracker/', include('requirementsTracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}),)
