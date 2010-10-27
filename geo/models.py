from django.db import models
from django.contrib.auth.models import User
from geofic.fic.models import *

class City(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length = 100)
    description = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()

class Location(models.Model):
    admin = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    city = models.ForeignKey(City)
    lat = models.FloatField()
    lon = models.FloatField()
    flagged = models.BooleanField(default = False)

class Coupon(models.Model):
    content = models.TextField()
    location = models.ForeignKey(Location)
