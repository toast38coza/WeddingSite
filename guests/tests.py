from django.test import TestCase, Client
from django.contrib.sites.models import Site
from website.models import Wedding 
from events.models import Event
from events.helpers import EventsMockDataHelper
from guests.models import *
from guests.helpers import EmailHelper
from django.core import mail
import unittest

class APITestCase(TestCase):

	def setUp(self):
		self.c = Client()
		self.site = Site.objects.create()
		self.wedding = Wedding.objects.create(site=self.site, intro="hello", partner_one="A", partner_two="B")

		for event in ["event1", "event2", "event3", "event4", "event5"]:
			EventsMockDataHelper.get_event(self.wedding, event)

	def test_rsvp_new_user(self):

		url = "/api/v1/guests/guests/rsvp/"
		data = {
			"rsvp-extra": "extra info",
			"rsvp-name": "Christo Crampton",
			"rsvp-email": "joe@soap.com",
			"event[]": ["1", "2", "3"]
		}

		response = self.c.post(url, data)
		created_guest = Guest.objects.get(email="joe@soap.com")
		rsvps = GuestRSVP.objects.filter(guest=created_guest)

		assert created_guest.last_name == "Crampton"
		assert response.status_code == 200, 'Expect 200 OK'

		assert len(rsvps) == 3

		assert len(mail.outbox) == 1, 'Expect mail to be sent to couple and guest'

		'''
		request.data
		MergeDict(<QueryDict: {u'rsvp-extra': [u'dsklfjaslf'], u'rsvp-name': [u'Test'], u'rsvp-email': [u'info@38.co.za']}>, <MultiValueDict: {}>)
		'''

class EmailHelperTestCase(TestCase):

	def setUp(self):
		self.helper = EmailHelper()

	@unittest.skip("..")
	def test_send_rsvp_to_couple(self):

		self.helper.send_rsvp_to_couple(guest)

		assert len(mail.outbox) == 1, 'Expect mail to be in outbox'