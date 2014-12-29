from django.db import models
from django.contrib.sites.models import Site
from autoslug import AutoSlugField

class Wedding(models.Model):

    def __unicode__(self):
        return "{0} & {1}'s Wedding" . format (self.partner_one, self.partner_two)

    site = models.ForeignKey('sites.Site')
    intro = models.TextField()
    headline = models.CharField(max_length=100)
    partner_one = models.CharField(max_length=100)
    partner_two = models.CharField(max_length=100)


    def get_enabled_sections(self):

        return Section.get_enabled(self.pk)

    def get_ceremony_venue(self):
        try:
            return WeddingCeremonyVenue.objects.get(wedding=self)
        except WeddingCeremonyVenue.DoesNotExist:
            return None

    def get_reception_venue(self):
        try:
            return WeddingReceptionVenue.objects.get(wedding=self)
        except WeddingReceptionVenue.DoesNotExist:
            return None


class CouplePhotos(models.Model):
    """
    These are photos that will be shown on the slider
    at the top of the page
    """
    wedding = models.ForeignKey('Wedding')
    title = models.CharField(max_length=100)

    caption = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='landing-page')


class WeddingCeremonyVenue(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('Wedding') ## OneToOne? 
    title = models.CharField(max_length=100)
    extra_info = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    address = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class WeddingReceptionVenue(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('Wedding')
    title = models.CharField(max_length=100)
    extra_info = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    address = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class Section(models.Model):

    def __unicode__(self):
        return self.headline

    wedding = models.ForeignKey('Wedding')
    
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=100, blank=True)

    headline = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='headline')

    tagline = models.CharField(max_length=100, blank=True)
    background_image = models.ImageField(upload_to='landing-page', blank=True)
    enabled = models.BooleanField(default=True, db_index=True)

    @property 
    def template_path(self):
        return "themes/bliss/partials/{0}.html" . format (self.slug)

    @staticmethod
    def get_enabled(wedding):
        return Section.objects.filter(wedding=wedding, enabled=True)


from website.signals import wedding_created