from django.shortcuts import render
from website.models import Wedding, Section, BridalPartyMember
from logistics.models import Accommodation, Attraction
from events.models import Event
from gallery.models import Gallery
from django.contrib.sites.shortcuts import get_current_site
from faq.models import FAQ


def _get_bridal_parties():

	her_side = {
		"bride": BridalPartyMember.get_bride()[0],
		"mom": BridalPartyMember.get_her_mom()[0],
		"dad": BridalPartyMember.get_her_dad()[0],
		"bridesmaids": BridalPartyMember.get_bridesmaids(),
	}
	his_side = {
		"groom": BridalPartyMember.get_groom()[0],
		"mom": BridalPartyMember.get_his_mom()[0],
		"dad": BridalPartyMember.get_his_dad()[0],
		"groomsmen": BridalPartyMember.get_groomsmen(),
	}

	return her_side, his_side

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
	galleries = Gallery.objects.filter(wedding=wedding)

	ceremony_venue = wedding.get_ceremony_venue()
	reception_venue = wedding.get_reception_venue()

	if ceremony_venue:
		wedding_date = ceremony_venue.start_datetime
	else: 
		wedding_date = None

	her_side, his_side = _get_bridal_parties()

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
		"her_side": her_side,
		"his_side": his_side,
		"galleries": galleries,
	}
	return render(request, "themes/bliss/index.html", context)
