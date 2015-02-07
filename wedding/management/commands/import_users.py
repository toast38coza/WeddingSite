from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from guests.models import *
from website.models import Wedding
import csv

class Command(BaseCommand):
    help = 'Sets up the initial data'

    def handle(self, *args, **options):

    	print "importing guests"
    	wedding = Wedding.objects.all()[0]

    	with open('guests.csv') as csvfile:
    		reader = csv.reader(csvfile)
    		for row in reader:
    			name = row[0]
    			print name

    			fname, sname = name.split(" ", 1)
    			email = row[4]
    			save_the_date = row[5]
    			rsvp = row[6]

    			rsvp_yes = rsvp == "yes"

    			#user, created = User.objects.get_or_create(email=email, first_name = fname, last_name=sname)

    			data = {
    				"first_name": fname,
    				"last_name": sname,
    				"email": email,
    				"coming_to_wedding": rsvp_yes,
    				#"user_id": user.pk,
    				"wedding_id": wedding.pk
    			}

    			Guest.objects.create(**data)
