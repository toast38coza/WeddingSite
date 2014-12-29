from django.contrib import admin

from website.models import Wedding, CouplePhotos, WeddingCeremonyVenue, WeddingReceptionVenue, Section

admin.site.register(Wedding)
admin.site.register(CouplePhotos)
admin.site.register(WeddingCeremonyVenue)
admin.site.register(WeddingReceptionVenue)
admin.site.register(Section)
