from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from website.api import UserViewSet, WeddingViewSet
from guests.api import guest_router

# api:
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'weddings', WeddingViewSet)



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^thanks/$', 'website.views.thanks', name='thanks'),

    url(r'^api/v1/guests/', include(guest_router.urls)),

    # api:
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)