from django.db import models


class Accommodation(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding') ## OneToOne? 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    #extra_info = models.TextField(blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField()


class Attraction(models.Model):

    def __unicode__(self):
        return self.title 

    wedding = models.ForeignKey('website.Wedding') ## OneToOne? 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    #extra_info = models.TextField(blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(blank=True)
    