from datetime import datetime
from website.models import *

class MockDataHelper:

	@staticmethod
	def get_wedding(site, intro="lorum ipsum", p1 = "Jane", p2 = "John"):
		return Wedding.objects.create(site=site, intro="hello", partner_one="A", partner_two="B")		

	@staticmethod
	def get_new_ceremony_venue(wedding, title=None, start_datetime = None, extra_info=None):

		if title is None:
			title = "Test ceremony venue"

		if extra_info is None:
			extra_info = "Lorum ipsum ..."

		if start_datetime is None:
			start_datetime = datetime.now()

		return WeddingCeremonyVenue.objects.create(wedding = wedding, title=title, \
			start_datetime = start_datetime, address="Swakopmund, Namibia", extra_info=extra_info, latitude = "0", longitude = "0")

	@staticmethod
	def get_new_reception_venue(wedding, title=None, start_datetime = None, extra_info=None):

		if title is None:
			title = "Test reception venue"

		if extra_info is None:
			extra_info = "Lorum ipsum ..."

		if start_datetime is None:
			start_datetime = datetime.now()

		return WeddingReceptionVenue.objects.create(wedding = wedding, title=title, \
			start_datetime = start_datetime, extra_info=extra_info, address="Swakopmund, Namibia", latitude = "0", longitude = "0")

