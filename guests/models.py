from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

GENDERS = [('Male','Male'), ('Female','Female')]

# Create your models here.
class Guest(models.Model):

    def __unicode__(self):
        return "{0} {1}" . format (self.first_name, self.last_name) 

    wedding = models.ForeignKey('website.Wedding')
    #user = models.OneToOneField(User)
    partner = models.ForeignKey('Guest', blank=True, null=True, default=None)

    # a unique code the guest can use to login
    guest_code = models.CharField(max_length=10, blank=True, null=True) 

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    vegetarian = models.BooleanField(default=False)
    is_family = models.BooleanField(default=False)
    gender = models.CharField(default='Female', choices=GENDERS, max_length=10)
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

