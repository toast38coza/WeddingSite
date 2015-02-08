from django.contrib import admin
from guests.models import * 

class GuestRSVPInline(admin.StackedInline):
    model = GuestRSVP


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'partner', 'coming_to_wedding')
    list_editable = ('first_name', 'last_name', 'email', 'partner', 'coming_to_wedding')
    list_filter = ('coming_to_wedding',)
    search_fields = ['first_name', 'last_name', 'email',]
    inlines = [GuestRSVPInline]

admin.site.register(Guest, GuestAdmin)

