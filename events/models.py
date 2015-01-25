from django.db import models

class Event(models.Model):

	def __unicode__(self):
		return self.title

	wedding = models.ForeignKey('website.Wedding') 
	title = models.CharField(max_length=100, help_text="The name of the venue")
	start_datetime = models.DateTimeField(help_text="When does the event start?")
	address = models.TextField(help_text="Address where this event will be held", blank=True)

	description = models.TextField(blank=True)
	picture = models.ImageField(upload_to='events', blank=True)
    

