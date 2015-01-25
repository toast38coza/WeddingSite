from django.shortcuts import render
from website.models import Wedding, Section
from logistics.models import Accommodation, Attraction
from events.models import Event
from django.contrib.sites.shortcuts import get_current_site
from faq.models import FAQ

def home(request):

	wedding = Wedding.objects.all()[0]

	sections = wedding.get_enabled_sections()
	num_sections = len(sections)
	midpoint = num_sections/2

	left_sections = sections[0:midpoint]
	right_sections = sections[midpoint:]

	faqs = FAQ.objects.filter(wedding=wedding)
	accommodations = Accommodation.objects.filter(wedding=wedding)
	attractions = Attraction.objects.filter(wedding=wedding)
	events = Event.objects.filter(wedding=wedding)

	ceremony_venue = wedding.get_ceremony_venue()
	reception_venue = wedding.get_reception_venue()

	if ceremony_venue:
		wedding_date = ceremony_venue.start_datetime
	else: 
		wedding_date = None

	context = {
		"wedding" : wedding,
		"sections": sections,
		"faqs": faqs,
		"accommodations": accommodations,
		"events": events,
		"attractions": attractions,
		"left_sections": left_sections,
		"right_sections": right_sections,
		"ceremony_venue": ceremony_venue,
		"reception_venue": reception_venue,
		"wedding_date": wedding_date,
	}
	return render(request, "themes/bliss/index.html", context)
