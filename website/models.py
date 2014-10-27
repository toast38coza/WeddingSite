from django.db import models
from django.contrib.sites.models import Site


class Wedding(models.Model):

    site = models.ForeignKey('sites.Site')
    into = models.TextField()
    partner_one = models.CharField(max_length=100)
    partner_two = models.CharField(max_length=100)


class CouplePhotos(models.Model):


    wedding = models.ForeignKey('Wedding')
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to='landing-page')


class WeddingCeremonyVenue(models.Model):

    wedding = models.ForeignKey('Wedding')
    title = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    address = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class WeddingReceptionVenue(models.Model):

    wedding = models.ForeignKey('Wedding')
    title = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    address = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class Section(models.Model):

    wedding = models.ForeignKey('Wedding')
    
    meta_title = models.CharField(max_length=100)
    meta_describption = models.CharField(max_length=100)

    headline = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)


