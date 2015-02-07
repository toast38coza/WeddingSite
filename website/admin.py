from django.contrib import admin

from website.models import Wedding, CouplePhotos, WeddingCeremonyVenue, WeddingReceptionVenue, Section, BridalPartyMember

class SectionAdmin(admin.ModelAdmin):
    exclude = ['meta_title', 'meta_description', 'background_image']

admin.site.register(Wedding)
#admin.site.register(CouplePhotos)
admin.site.register(WeddingCeremonyVenue)
admin.site.register(WeddingReceptionVenue)
admin.site.register(BridalPartyMember)
admin.site.register(Section, SectionAdmin)
