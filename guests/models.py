from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Guest(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding')
    user = models.OneToOneKey(User)
    partner = models.ForeignKey('Guest')

    # a unique code the guest can use to login
    guest_code = models.CharField(max_length=10) 

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    has_been_emailed = models.BooleanField(default=False)
    has_logged_into_site = models.BooleanField(default=False)

    tags = TaggableManager()
    
class GuestRSVP(models.Model):

	guest = models.ForeignKey('Guest')
	event = models.ForeignKey('events.Event')

	rsvp = models.BooleanField(default=False)


