from django.contrib import admin
from guests.models import * 

class GuestRSVPInline(admin.StackedInline):
    model = GuestRSVP


class GuestAdmin(admin.ModelAdmin):
    inlines = [GuestRSVPInline]

admin.site.register(Guest, GuestAdmin)

