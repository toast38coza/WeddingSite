from django.db import models
from autoslug import AutoSlugField

class Gallery(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding') 
    title = models.CharField(max_length=100, help_text="The name of the gallery")
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(help_text="The order in which to show these galleries")
    
class Picture(models.Model):

	def __unicode__(self):
		return self.caption

	gallery = models.ForeignKey(Gallery)
	image = models.ImageField(upload_to='photogallery')
	caption = models.TextField(blank=True, null = True)
	cover_picture = models.BooleanField(default=False)
