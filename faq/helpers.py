from faq.models import FAQ

def get_data(wedding, title=None, description=None):

	if title is None:
		title = "Some question ..."

	if description is None:
		description = "lorum ipsum"

	return {
		"wedding": wedding, 
		"title": title,
		"description": description,
	}

class FAQMockDataHelper:

	@staticmethod
	def get_faq(wedding, title=None, description=None):

		data = get_data(wedding)
		FAQ.objects.create(**data)