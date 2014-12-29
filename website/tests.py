from django.test import TestCase, Client
from website.models import Wedding, Section, WeddingCeremonyVenue, WeddingReceptionVenue
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from mock import patch
from website.helpers import MockDataHelper

###
# Views
###

class WeddingHomePageViewTests(TestCase):

	def setUp(self):
		self.site = Site.objects.create()
		self.wedding = Wedding.objects.create(site=self.site, intro="hello", partner_one="A", partner_two="B")

	def test_page_selects_the_correct_wedding(self):
		pass

	def test_page_loads(self):

		c = Client() 
		url = reverse("home")
		response = c.get(url)

		assert response.status_code == 200, "Expect 200 OK" 
		expected_context_variables = ["wedding", "sections", "left_sections", "right_sections"]
		for var in expected_context_variables:
			
			assert var in response.context,\
				"Expect {0} to be in context" . format (var) 


###
# Models
###

class WeddingModelTests(TestCase):

	def setUp(self):
		self.site = Site.objects.create()
		self.wedding = wedding = Wedding.objects.create(site=self.site, intro="hello", partner_one="A", partner_two="B")

	def test_create_wedding_creates_default_sections(self):

		assert len(self.wedding.section_set.all()) == 5		

	def test_get_enabled_sections(self):

		wedding = Wedding.objects.create(site=self.site, intro="hello", partner_one="A", partner_two="B")		
		sections = wedding.get_enabled_sections()

		for section in sections: 

			assert section.wedding_id == wedding.pk, "Expect All ids should to be this wedding"
			assert section.enabled is not False, "Expect only enabled sections"

	def test_get_ceremony_venue_none_if_not_exists(self):

		venue = self.wedding.get_ceremony_venue()
		assert venue is None, "Expect None if there is no venue defined"

	def test_get_ceremony_venue_returns_venue(self):

		wedding1 = MockDataHelper.get_wedding(self.site)
		wedding2 = MockDataHelper.get_wedding(self.site)

		venue1 = MockDataHelper.get_new_ceremony_venue(wedding1)
		venue2 = MockDataHelper.get_new_ceremony_venue(wedding2)

		venue = wedding1.get_ceremony_venue()

		assert isinstance(venue, WeddingCeremonyVenue), "Expect it to return a WeddingCeremonyVenue"
		assert venue == venue1, "Expect it to return the correct venue"


class SectionModelTests(TestCase):

	def setUp(self):

		site = Site.objects.create()
		self.wedding = Wedding.objects.create(site=site, intro="hello", partner_one="A", partner_two="B")	

	def test_get_enabled_gets_only_enabled_sites(self):
		"""
		Section.get_enabled returns only enabled sites
		"""
		site = Site.objects.create()
		new_wedding = Wedding.objects.create(site=site, intro="hello", partner_one="A1", partner_two="B1")

		data = {
			"tagline": "tagline",
			"wedding": self.wedding
		}

		s1 = Section.objects.create \
				(headline="s1", tagline="s1 tagline", wedding=self.wedding, enabled=True)
		s2 = Section.objects.create \
				(headline="s2", tagline="s1 tagline", wedding=self.wedding, enabled=False)
		
		enabled_sections = Section.get_enabled(self.wedding)

		ids = [item.get('id') for item in enabled_sections.values()]
		
		assert s1.pk in ids, "Expect enabled section to be shown"
		assert s2.pk not in ids, "Expect disabled section not to be returned"

		assert enabled_sections.filter(wedding=new_wedding).count() == 0, \
					"Expect that only items from the passed in wedding are included"

