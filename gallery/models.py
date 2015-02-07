from django.db import models

class Gallery(models.Model):

    def __unicode__(self):
        return self.title 

    title = models.CharField(max_length=100, help_text="The name of the venue")
    description = models.TextField(blank=True, help_text="Some extra info about it. Maybe what it looks like, or something cool about the place")
    order = models.PositiveIntegerField(help_text="The order in which to show these galleries")
    
class Picture(models.Model):

	def __unicode__(self):
		return self.caption

	image = models.ImageField(upload_to='photogallery')
	caption = models.TextField(blank=True, null = True)
	cover_picture = models.BooleanField(default=False)
