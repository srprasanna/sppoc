from django.conf.urls import patterns, url
from venueregistration.views import ManagerList, LocationList, VenueTypeList, EventTypeList, VenueList

urlpatterns = patterns('',

                       url(r'^managers/$', ManagerList.as_view(), name='manager_list'),
                       url(r'^locations/$', LocationList.as_view(), name='location_list'),
                       url(r'^venuetypes/$', VenueTypeList.as_view(), name='venuetype_list'),
                       url(r'^eventtypes/$', EventTypeList.as_view(), name='eventtype_list'),
                       url(r'^venues/$', VenueList.as_view(), name='venue_list'),



                       )