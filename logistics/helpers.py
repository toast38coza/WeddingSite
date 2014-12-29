from logistics.models import Accommodation, Attraction

def get_data(wedding, title=None, description=None, address=None, website=None, picture=None):

	if title is None:
		title = "Some Hotel"

	if description is None:
		description = "lorum ipsum"

	if address is None:
		address = "Some street, somewhere"

	if website is None:
		website = "http://www.google.com" 

	return {
		"wedding": wedding, 
		"title": title,
		"description": description,
		"address": address,
		"website": website,
		"picture": picture
	}

class LogisticsMockDataHelper:

	@staticmethod
	def get_attraction(wedding, title=None, description=None, address=None, website=None, picture=None):

		data = get_data(wedding)
		Attraction.objects.create(**data)


	@staticmethod
	def get_accommodation(wedding, title=None, description=None, address=None, website=None, picture=None):

		data = get_data(wedding)
		Accommodation.objects.create(**data)


	

		