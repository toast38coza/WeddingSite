from django.contrib import admin
from gallery.models import Gallery, Picture

class PictureInline(admin.StackedInline):
    model = Picture
    extra = 3

class GalleryAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

admin.site.register(Gallery, GalleryAdmin)


