from django.db import models
from django.contrib.sites.models import Site
from autoslug import AutoSlugField

class Wedding(models.Model):

    def __unicode__(self):
        return "{0} & {1}'s Wedding" . format (self.partner_one, self.partner_two)

    site = models.ForeignKey('sites.Site', help_text="Don't worry about this one ..")
    intro = models.TextField(help_text="This is the text that shows up as the welcome message")
    headline = models.CharField(max_length=100, help_text="The heading to your welcome message. Something like: 'We're getting married' works well")
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

    wedding = models.ForeignKey('Wedding') 
    title = models.CharField(max_length=100, help_text="The name of the venue")
    extra_info = models.TextField(blank=True, help_text="Some extra info about it. Maybe what it looks like, or something cool about the place")
    start_datetime = models.DateTimeField(help_text="When does the ceremony start?")
    address = models.TextField(help_text="What is the address for this venue")
    latitude = models.CharField(max_length=100, help_text="The latitude (you can get this off google maps) - it will be used to render the map on this page")
    longitude = models.CharField(max_length=100, help_text="The longitude (you can get this off google maps) - it will be used to render the map on this page")

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

    class Meta:
        ordering = ['order']

    wedding = models.ForeignKey('Wedding')
    
    meta_title = models.CharField(max_length=100, blank=True )
    meta_description = models.CharField(max_length=100, blank=True)

    headline = models.CharField(max_length=100, help_text="This is what will show as the heading for this section. e.g.: 'Logistics'")
    slug = AutoSlugField(populate_from='headline')
    tagline = models.CharField(max_length=100, blank=True, help_text="Put something here if you want to add a little context to the headline. 'Venues, accommodation and things to do'")
    
    background_image = models.ImageField(upload_to='landing-page', blank=True)
    enabled = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(help_text="Order in which you would like to display sections", default=100)

    @property 
    def template_path(self):
        return "themes/bliss/partials/{0}.html" . format (self.slug)

    @staticmethod
    def get_enabled(wedding):
        return Section.objects.filter(wedding=wedding, enabled=True)

BRIDAL_PARTY_OPTIONS = [
    ('Bride', 'Bride'), 
    ('Groom', 'Groom'), 
    ('Mom', 'Mom'), 
    ('Dad', 'Dad'), 
    ('Bridesmaid', 'Bridesmaid'), 
    ('Groomsman', 'Groomsman')]

SIDES = [('His','His'), ('Hers','Hers')]

class BridalPartyMember(models.Model):

    def __unicode__(self):
        return self.full_name

    role = models.CharField(max_length=100, choices=BRIDAL_PARTY_OPTIONS)
    side = models.CharField(max_length=100, choices=SIDES)
    role_detail = models.CharField(max_length=100, help_text="For example, 'Mother', 'Father', 'Maid of Honor' or 'Best Man'", blank=True, null=True)

    full_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="bridalparty", blank=True)

    ## Her Side
    @staticmethod
    def get_bride():
        return BridalPartyMember.get_role('Bride', 'Hers')

    @staticmethod
    def get_her_mom():
        return BridalPartyMember.get_role('Mom', 'Hers')

    @staticmethod
    def get_her_dad():
        return BridalPartyMember.get_role('Dad', 'Hers')

    @staticmethod
    def get_bridesmaids():
        return BridalPartyMember.get_role('Bridesmaid', 'Hers')

    ## His Side
    @staticmethod
    def get_groom():
        return BridalPartyMember.get_role('Groom', 'His')

    @staticmethod
    def get_his_mom():
        return BridalPartyMember.get_role('Mom', 'His')
    
    @staticmethod
    def get_his_dad():
        return BridalPartyMember.get_role('Dad', 'His')

    @staticmethod
    def get_groomsmen():
        return BridalPartyMember.get_role('Groomsman', 'His')

    @staticmethod 
    def get_role(role, side):
        return BridalPartyMember.objects.filter(role=role, side=side)

from website.signals import wedding_created





