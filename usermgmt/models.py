from django.db import models
from django.contrib.auth.models import User
from geofic.geo.models import *
from geofic.fic.models import *

class Profile(models.Model):
    gender_choices = (
            (0, "Male"),
            (1, "Female"),
            (2, "Transgender")
            )
    orientation_choices = (
            (0, "Straight"),
            (1, "Bisexual"),
            (2, "Gay/Lesbian")
            )
    relationship_choices = (
            (0, "Single"),
            (1, "Dating"),
            (2, "Married"),
            (3, "Other - unavailable"),
            (4, "Other - available")
            )

    user = models.ForeignKey(User)
    bio = models.TextField(blank = True)
    home_city = models.ForeignKey(City, null = True, related_name = 'residing_participants')
    working_city = models.ForeignKey(City, null = True, related_name = 'working_participants')
    gender = models.IntegerField(choices = gender_choices, null = True)
    orientation = models.IntegerField(choices = orientation_choices, null = True)
    relationship_status = models.IntegerField(choices = relationship_choices, null = True)
    date_of_birth = models.DateField()
    utilized_coupons = models.ManyToManyField(Coupon)
    ctime = models.DateTimeField(auto_now_add = True)

class StoryRun(models.Model):
    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    start_time = models.DateTimeField(auto_now_add = True)
    end_time = models.DateTimeField(null = True)
    valid = models.BooleanField()

class CompletedChapter(models.Model):
    chapter = models.ForeignKey(Chapter)
    story_run = models.ForeignKey(StoryRun)
    time_completed = models.DateTimeField(auto_now_add = True)
