from django.conf.urls.defaults import *

urlpatterns = patterns('geofic.geo.views',
    (r'^(location/)?(?P<location_id>\d+)/$', 'show_location'),
    (r'^city/(?P<city_slug>.+)/$', 'show_city'),
    (r'^edit/(?P<location_id>\d+)/$', 'edit_location'),
    (r'^edit(?P<city_slug>.+)/$', 'edit_city'),
    (r'^delete/(?P<location_id>\d+)/$', 'delete_location'),
    (r'^delete/(?P<city_slug>.+)/$', 'delete_city'),
    (r'^contribute/location/$', 'add_location'),
    (r'^contribute/city/$', 'add_city'),
    (r'^contribute/coupon/$', 'add_coupon'),
    (r'^flag/(?P<location_id>\d+)/', 'flag_location'),
)
