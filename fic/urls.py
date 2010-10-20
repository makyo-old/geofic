from django.conf.urls.defaults import *

urlpatterns = patterns('geofic.fic.views',
    (r'^story/(?P<story_id>\d+)/$', 'show_story'),
    (r'^chapter/(?P<chapter_id>\d+)/$', 'show_chapter_by_id'),
    (r'^(?P<story_id>\d+)/(?P<chapter_number>\d+)/$', 'show_chapter_by_number'),
    (r'^genre/(?P<genre>.+)/$', 'list_stories_by_genre'),
    (r'^rating/(?P<rating_level>(general|mature|adult))/$', 'list_stories_by_rating'),
    (r'^contribute/story/$', 'add_story'),
    (r'^contribute/chapter/(?P<story_id>\d+)/$', 'add_chapter'),
    (r'^edit/story/(?P<story_id>\d+)/$', 'edit_story'),
    (r'^edit/chapter/(?P<chapter_id>\d+)/$', 'edit_chapter'),
    (r'^delete/story/(?P<story_id>\d+)/$', 'delete_story'),
    (r'^delete/chapter/(?P<chapter_id>\d+)/$', 'delete_chapter')
)
