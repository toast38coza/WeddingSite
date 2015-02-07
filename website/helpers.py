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

	@staticmethod
	def create_bridal_parties(num_bridesmaids = 3, num_groomsmen=3):

		BridalPartyMember.objects.create(role='Bride', side='Hers', full_name='Tammy')
		BridalPartyMember.objects.create(role='Groom', side='His', full_name='Mike')

		BridalPartyMember.objects.create(role='Mom', side='Hers', full_name='Mrs. Arendse')
		BridalPartyMember.objects.create(role='Dad', side='Hers', full_name='Mr. Arendse')

		BridalPartyMember.objects.create(role='Mom', side='His', full_name='Mrs. Kivido')
		BridalPartyMember.objects.create(role='Dad', side='His', full_name='Mr. Kivido')

		for x in range(0,num_bridesmaids):
			full_name='Bridesmaid {0}' . format (x)
			BridalPartyMember.objects.create(role='Bridesmaid', side='Hers', full_name = full_name)

		for x in range(0,num_groomsmen):
			full_name='Groomsman {0}' . format (x)
			BridalPartyMember.objects.create(role='Groomsman', side='His', full_name = full_name)
