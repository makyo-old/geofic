from django.db import models
from django.contrib.auth.models import User
from geofic.geo import *

class Story(models.Model):
    title
    blurb
    genres
    description
    author
    bibliography
    city
    ctime

class Chapter(models.Model):
    number
    title
    body
    location
