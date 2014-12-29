from django.contrib.auth.models import User
from website.models import Wedding
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding        


# ViewSets define the view behavior.
class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer

