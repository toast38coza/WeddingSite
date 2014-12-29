from django.core.management.base import BaseCommand, CommandError
from website.models import Wedding
from website.helpers import MockDataHelper
from logistics.helpers import LogisticsMockDataHelper
from faq.helpers import FAQMockDataHelper
from django.contrib.sites.models import Site
from datetime import datetime


class Command(BaseCommand):
    help = 'Sets up the initial data'

    def handle(self, *args, **options):

        for w in Wedding.objects.all():
            w.delete()

        site = Site.objects.all()[0]

        intro = """
Cupcake ipsum dolor. Sit amet applicake. 
Cotton candy I love ice cream lollipop pie I love jujubes. 
Muffin I love toffee sesame snaps macaroon I love biscuit. 
Lollipop chocolate cake candy. 
Lemon drops cotton candy apple pie gummi bears lemon drops gummi bears.
"""

        wedding = Wedding.objects.create(
            site=site, intro=intro, partner_one="Tammy", partner_two="Michael")

        start_datetime = datetime(2015, 9, 26)

        MockDataHelper.get_new_ceremony_venue(
            wedding, start_datetime=start_datetime)
        MockDataHelper.get_new_reception_venue(
            wedding, start_datetime=start_datetime)

        LogisticsMockDataHelper.get_attraction(wedding)
        LogisticsMockDataHelper.get_attraction(wedding)
        LogisticsMockDataHelper.get_attraction(wedding)
        LogisticsMockDataHelper.get_attraction(wedding)

        LogisticsMockDataHelper.get_accommodation(wedding)
        LogisticsMockDataHelper.get_accommodation(wedding)
        LogisticsMockDataHelper.get_accommodation(wedding)
        LogisticsMockDataHelper.get_accommodation(wedding)

        for x in range(0, 5):

            title = "Question no #{0}" . format (x)
            description = intro

            FAQMockDataHelper.get_faq(
                wedding, title=title, description=description)
