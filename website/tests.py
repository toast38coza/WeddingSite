from django.test import TestCase, Client
from website.models import Wedding, Section, WeddingCeremonyVenue, WeddingReceptionVenue, BridalPartyMember
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

	def test_get_bridal_parties_gets_her_side(self):

		num_bridesmaids = 2
		num_groomsmen = 0

		MockDataHelper.create_bridal_parties(num_bridesmaids, num_groomsmen)

		from website.views import _get_bridal_parties
		her_side, his_side = _get_bridal_parties()

		assert her_side.get("mom").full_name == 'Mrs. Arendse'
		assert her_side.get("dad").full_name == 'Mr. Arendse'
		assert len(her_side.get("bridesmaids")) == num_bridesmaids

	def test_get_bridal_parties_gets_his_side(self):

		num_bridesmaids = 0
		num_groomsmen = 4

		MockDataHelper.create_bridal_parties(num_bridesmaids, num_groomsmen)

		from website.views import _get_bridal_parties
		her_side, his_side = _get_bridal_parties()

		assert his_side.get("mom").full_name == 'Mrs. Kivido'
		assert his_side.get("dad").full_name == 'Mr. Kivido'
		assert len(his_side.get("groomsmen")) == num_groomsmen

	def test_page_loads(self):

		MockDataHelper.create_bridal_parties()
		c = Client() 
		url = reverse("home")
		response = c.get(url)

		assert response.status_code == 200, "Expect 200 OK" 
		expected_context_variables = ["wedding", "sections", "left_sections", 
									  "right_sections", "accommodations", "faqs",
									  "attractions", "her_side", "his_side"]

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

		assert len(self.wedding.section_set.all()) > 0		

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

	def test_get_bride(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_bride()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Tammy'

	def test_get_her_dad(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_groom()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Mike'

	def test_get_her_mom(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_her_mom()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Mrs. Arendse'

	def test_get_her_dad(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_her_dad()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Mr. Arendse'

	def test_get_his_mom(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_his_mom()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Mrs. Kivido'

	def test_get_his_dad(self):

		MockDataHelper.create_bridal_parties()

		person = BridalPartyMember.get_his_dad()
		assert len(person) == 1, 'Returns only 1 value'
		assert person[0].full_name == 'Mr. Kivido'


class SectionModelTests(TestCase):

	def setUp(self):

		site = Site.objects.create()
		self.wedding = Wedding.objects.create(site=site, intro="hello", partner_one="A", partner_two="B")	

	def test_get_enabled_results_are_ordered_by_order(self):

		# remove sections:
		for s in Section.objects.all(): s.delete()

		s2 = Section.objects.create(headline="s2", tagline="", wedding=self.wedding, enabled=True, order=2)
		s1 = Section.objects.create(headline="s1", tagline="", wedding=self.wedding, enabled=True, order=1)
		s3 = Section.objects.create(headline="s3", tagline="", wedding=self.wedding, enabled=True, order=3)

		sections = Section.get_enabled(self.wedding)

		assert len(sections) == 3, 'Expect 3 sections to be returned'

		names_in_order = [section.headline for section in sections]

		self.assertEqual(['s1','s2','s3'], names_in_order)



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

