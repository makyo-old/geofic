from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^geo/', include("geofic.geo.urls")),
    (r'^fic/', include("geofic.fic.urls")),
    (r'^user/', include("geofic.usermgmt.urls")),
    (r'^accounts/', include("geofic.usermgmt.account_urls"))
)
