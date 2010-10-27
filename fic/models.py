from django.db import models
from django.contrib.auth.models import User
from geofic.geo import *

class Story(models.Model):
    rating_choices = (
            (0, 'General - all audiences'),
            (1, 'Mature - some mature content'),
            (2, 'Adult - very mature content')
            )
    transportation_choices = (
            (0, 'Walking'),
            (1, 'Biking'),
            (2, 'Driving'),
            (3, 'Public transit')
            )

    title = models.CharField(max_length = 200)
    blurb = models.TextField()
    genres = models.CharField(max_length = 500)
    rating = models.IntegerField(choices = rating_choices)
    min_age = models.IntegerField(null = True)
    description = models.TextField()
    author = models.ForeignKey(User)
    bibliography = models.TextField()
    city = models.ForeignKey(City)
    ctime = models.DateTimeField(auto_now_add = True)
    distance = models.FloatField(null = True)
    complete = models.BooleanField(default = True)
    transportation_type = models.IntegerField(choices = transportation_choices)

class Chapter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length = 200)
    body = models.TextField()
    location = models.ForeignKey(Location, null = True)
