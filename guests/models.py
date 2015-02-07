from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Guest(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding')
    #user = models.OneToOneField(User)
    partner = models.ForeignKey('Guest', blank=True, null=True, default=None)

    # a unique code the guest can use to login
    guest_code = models.CharField(max_length=10, blank=True, null=True) 

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    vegetarian = models.BooleanField(default=False)
    coming_to_wedding = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    has_been_emailed = models.BooleanField(default=False)
    has_logged_into_site = models.BooleanField(default=False)

    tags = TaggableManager()
    
class GuestRSVP(models.Model):

    class Meta:
        unique_together = ("guest", "event")


    guest = models.ForeignKey('Guest')
    event = models.ForeignKey('events.Event')

    rsvp = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class BridalPartyPerson(models.Model):

    wedding = models.ForeignKey('website.Wedding')
    user = models.OneToOneField(User)
    guest = models.ForeignKey('Guest')

    description = models.TextField(blank=True)

    picture = models.ImageField(upload_to='picture', blank=True)

