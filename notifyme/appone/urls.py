from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from . import viewsclgs
from . import viewsclgtags
from . import viewsdetails
from . import viewsevents
from . import viewstags
from . import viewsfollows

urlpatterns = [
   re_path(r'^colleges/(?P<pk>[0-9]+)$',viewsclgs.get_delete_update_clgs.as_view(),name='get_delete_update_colleges'),
   url(r'^colleges/',viewsclgs.get_post_clgs.as_view(),name='get_post_colleges'),    
   url(r'^collegetags/',viewsclgtags.get_post_clgtags.as_view(),name='get_post_collegetags'),    
   re_path(r'^details/(?P<pk>[0-9]+)$',viewsdetails.get_delete_update_details.as_view(),name='get_delete_update_details'),
   url(r'^details/',viewsdetails.get_post_details.as_view(),name='get_post_details'),    
   re_path(r'^events/(?P<pk>[0-9]+)$',viewsevents.get_delete_update_events.as_view(),name='get_delete_update_events'),
   url(r'^events/',viewsevents.get_post_events.as_view(),name='get_post_events'),    
     re_path(r'^follows/(?P<pk>[0-9]+)$',viewsfollows.get_delete_update_follows.as_view(),name='get_delete_update_follows'),
   url(r'^follows/',viewsfollows.get_post_follows.as_view(),name='get_post_follows'),
   re_path(r'^tags/(?P<pk>[0-9]+)$',viewstags.get_delete_update_tags.as_view(),name='get_delete_update_tags'),
   url(r'^tags/',viewstags.get_post_tags.as_view(),name='get_post_tags'),    
]
