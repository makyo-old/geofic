from django.conf.urls.defaults import *

urlpatterns = patterns('geofic.fic.views',
    (r'^story/(?P<story_id>\d+)/$', 'show_story'),
    (r'^chapter/(?P<chapter_id>\d+)/$', 'show_chapter_by_id'),
    (r'^(?P<story_id>\d+)/(?P<chapter_number>\d+)/$', 'show_chapter_by_number'),
    (r'^genre/(?P<genre>.+)/$', 'list_stories_by_genre'),
    (r'^rating/(?P<rating_level>(general|mature|adult))/$', 'list_stories_by_rating')
)
