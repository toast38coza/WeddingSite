from events.models import Event 

from datetime import date
import random

def get_random_date():
	start_date = date.today().replace(day=1, month=1).toordinal()
	end_date = date.today().toordinal()
	return date.fromordinal(random.randint(start_date, end_date))

class EventsMockDataHelper:

	@staticmethod
	def get_event(wedding, title, start_datetime=None, description=None, address=None):

		if description is None:
			description = "lorum ipsum"

		if address is None:
			address = "Some street, somewhere"


		if start_datetime is None:
			start_datetime = get_random_date()


		data = {
			"wedding": wedding,
			"title": title,
			"start_datetime": start_datetime, 
			"description": description,
			"address": address,
		}

		Event.objects.create(**data)