from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^glogo/', include('glogo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('groups.urls')),
    (r'^logo/', include('glogo.urls')),
    
    ( r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT} ),
)


