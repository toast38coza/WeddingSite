from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage


class EmailHelper:

    def _send_message(self, subject, from_email, to, heading, content):

        msg = EmailMessage(subject=subject, from_email=from_email, to=to)
        msg.template_name = "BASIC"           # A Mandrill template name
        msg.template_content = {                        # Content blocks to fill in
            'HEADING': heading,
            'CONTENT': content
        }
        msg.global_merge_vars = {                       # Merge tags in your template
            'HEADING': heading,
            'CONTENT': content
        }
        msg.merge_vars = {}
        msg.send()


    def send_rsvp_to_couple(self, guest):
        #send_mail("It works!", "This will get sent through Mandrill",
        #"Djrill Sender <djrill@example.com>", ["info@38.co.za"])
        
        subject = "{0} {1} has RSVPed" .format (guest.first_name, guest.last_name)
        to = ['tamathamari@gmail.com', 'Michael.Kivido@bain.com']
        #to = ['info@38.co.za']
        from_email = "website@tammyandmichael.us"

        rsvps = guest.guestrsvp_set.all()
        event_string = ""
        for rsvp in rsvps:
            event_string += "<li>{0}</li>" . format (rsvp.event.title)

        content = '''
{0} {1} has RSVPed:<br/<br/> 

Coming to the wedding: {2}<br/<br/>

Events they're interested in: {3}<br/<br/>

Notes: {4}<br/<br/>

Details: http://tammyandmichael.us/admin/guests/guest/{5}/

With love from the website
''' . format (guest.first_name, guest.last_name, guest.coming_to_wedding, event_string, guest.notes, guest.pk)

        heading = "RSVP"

        self._send_message(subject, from_email, to, heading, content)

        

        

    def send_rsvp_to_guest(self):
        send_mail("It works!", "This will get sent through Mandrill",
        "Djrill Sender <djrill@example.com>", ["info@38.co.za"])

        