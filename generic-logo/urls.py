from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from views import *

urlpatterns = patterns('',
    url(r'^(?P<logo_id>\d+)/set-primary/$', select_primary, name="select_primary"),
    url(r'^(?P<logo_id>\d+)/delete/$', delete_logo, name="delete_logo"),
)
