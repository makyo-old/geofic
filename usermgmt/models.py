from django.db import models
from django.contrib.auth.models import *
from geofic.geo.models import *
from geofic.fic.models import *

class Profile(models.Model):
    user
    bio
    hometown
    gender
    orientation
    marital_status
    utilized_coupons

class StoryRun(models.Model):
    user
    story
    start_time
    end_time
    valid

class CompletedChapter(models.Model):
    chapter
    story_run
    time_completed
