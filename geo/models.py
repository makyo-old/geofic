from django.db import models
from django.contrib.auth.models import User
from geofic.fic.models import *

class City(models.Model):
    slug
    name
    description
    point

class Location(models.Model):
    name
    description
    city
    point

class Coupon(models.Model):
    content
    location
