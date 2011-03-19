from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

from views import *

urlpatterns = patterns('',
    url(r'^$', groups, name='groups'),
    url(r'^(?P<group_id>\d+)/detail/$', group, name="group"),
)
