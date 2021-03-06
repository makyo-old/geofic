from geofic.geo.models import *
from geofic.fic.models import *
from geofic.usermgmt.models import *
from datetime import datetime
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

@login_required
def show_location(request, location_id):
    # Grab the location
    location = get_object_or_404(Location, id = location_id)

    # Grab the user's current stories
    pertinent_stories = request.user.profile.storyrun_set.filter(active__eq = True).filter(story__city__eq = location.city)
    chapters = []
    for story in pertinent_stories:
        
        # Grab the next chapter in the story - if it's in the location, drop it in `chapters' and mark it as completed
        next_chapter = Chapter.objects.filter(story__eq = story.story).filter(number__eq = story.completedchapter_set.count() - 1)
        if (next_chapter and next_chapter.location == location):
            chapters.append(next_chapter)
            complete = CompletedChapter(chapter = next_chapter, story_run = story)
            complete.save()

            # finish the story if it's the last chapter and the story's complete (i.e.: no more chapters will be added)
            if (next_chapter.number == story.story.chapter_set.count() and story.story.complete):
                story.end_time = datetime.datetime()
                story.active = False
                story.save()
    return render_to_response("geo/location.html", context_instance = RequestContext(request, {'chapters': chapters}))

def show_city(request, city_slug):
    # Grab the city and render it
    city = get_object_or_404(City, slug = city_slug)
    return render_to_response("geo/city.html", context_instance = RequestContext(request, {'city': city}))

@login_required
def edit_location(request, location_id):
    # Grab the location and make sure the user can edit it
    location = get_object_or_404(Location, id = location_id)
    if (not (request.user.is_staff() or request.user == location.admin)):
        request.user.message_set.create(message = '<div class="error">' + _("Permission denied") + '</div>')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    # Show the form if no data is submitted, otherwise, save the data
    if (request.method == 'GET'):
        return render_to_response("geo/forms/location.html", context_instance = RequestContext(request, {'location': location, 'edit': True}))
    else:
        # save

@login_required
def edit_city(request, city_slug):
    # Grab the city and make sure the user can edit it
    city = get_object_or_404(City, slug = city_slug)
    if (not request.user.is_staff()):
        request.user.message_set.create(message = '<div class="error">' + _("Permission denied") + '</div>')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    # Show the form if no data is submitted, otherwise, save the data
    if (request.method == 'GET'):
        return render_to_response("geo/forms/city.html", context_instance = RequestContext(request, {'city': city, 'edit': True}))
    else:
        # save

@login_required
def edit_coupon(request, coupon_id):
    pass

@login_required
def delete_location(request, location_id):
    pass

@login_required
def delete_city(request, city_slug):
    pass

@login_required
def delete_coupon(request, coupon_id):
    pass

@login_required
def add_location(request):
    pass

@login_required
def add_city(request):
    pass

@login_required
def add_coupon(request):
    pass

@login_required
def flag_location(request, location_id):
    pass
