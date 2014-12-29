from django.db import models
from autoslug import AutoSlugField


class FAQ(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding')
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')

    description = models.TextField()

