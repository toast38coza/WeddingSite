from django.contrib.auth.models import User
from guests.models import Guest, GuestRSVP
from website.models import Wedding
from events.models import Event
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from guests.helpers import EmailHelper

# Serializers define the API representation.
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest



# ViewSets define the view behavior.
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    @list_route(methods=['get'])
    def email(self, request):

        email_helper = EmailHelper()
        email_helper.send_rsvp_to_couple()

        return Response('sent')


    @list_route(methods=['post'])
    def rsvp(self, request):

        '''
        event[]:Post wedding trips
        event[]:Family Dinner
        event[]:Boat Cruise
        rsvp-name:Christo Crampton
        rsvp-email:info@38.co.za
        rsvp-extra:extra requirements / messages
        '''

        rsvp_yes = request.POST.get("wedding-rsvp", False) == "yes"
        email = request.POST.get("rsvp-email", False)
        name = request.POST.get("rsvp-name", False)
        extra = request.POST.get("rsvp-extra", False)
        events = request.POST.getlist("event[]", [])
        
        
        ## hack ...
        wedding = Wedding.objects.all()[0]

        ## find or create the guest: 
        guest, created = Guest.objects.get_or_create(email=email, wedding=wedding)

        if created:
            if " " in name:
                first_name, last_name = name.split(" ", 1)
            else:
                first_name = name 
                last_name = None
            
            guest.first_name = first_name 
            guest.last_name = last_name

        for event_id in events:
            event = Event.objects.get(pk=event_id)
            rsvp, created = GuestRSVP.objects.get_or_create(guest=guest, event = event)
            rsvp.rsvp = True 
            rsvp.save()

        
        guest.coming_to_wedding = rsvp_yes         
        guest.notes = extra 
        guest.save()

        # send emails
        email_helper = EmailHelper()
        email_helper.send_rsvp_to_couple(guest)
        #email_helper.send_rsvp_to_guest()


    	return Response('sent')


class GuestRSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestRSVP


# ViewSets define the view behavior.
class GuestRSVPViewSet(viewsets.ModelViewSet):
    queryset = GuestRSVP.objects.all()
    serializer_class = GuestRSVPSerializer

guest_router = routers.DefaultRouter()
guest_router.register(r'guests', GuestViewSet)
guest_router.register(r'guests/rsvp', GuestRSVPViewSet)