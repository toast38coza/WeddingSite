from django.db.models.signals import post_save
from django.dispatch import receiver
from website.models import Wedding, Section
from django.conf import settings


@receiver(post_save, sender=Wedding, dispatch_uid="website.wedding.created")
def wedding_created(sender, instance, **kwargs):
    
    
    if kwargs.get("created", False) == True:

    	for section, enabled in settings.WEDDING_SECTIONS:
    		Section.objects.create(wedding = instance, headline=section, enabled=enabled)


