from django.conf.urls import *
from django.http import *
from django.views.generic.base import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rct/', include('rct.urls')),
    url('', include('social_auth.urls')),
    url(r'', include('social_auth.urls')),

    # url(r'^$', 'requirementsTracker.views.home', name='home'),
    # url(r'^requirementsTracker/', include('requirementsTracker.foo.urls')),
)

# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}),)
