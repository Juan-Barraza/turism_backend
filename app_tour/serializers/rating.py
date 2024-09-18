from rest_framework import serializers
from ..models import Rating
from .user import ListUserSerializers
from .place import ListPlaceSerializer

class ListRatingSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()
    users = ListUserSerializers()

    class Meta:
        model = Rating
        fields = (
            "id",
            "rating",
            "review",
            "users",
            "date",
            "places"
        )

class CreateRatingSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()
    users = ListUserSerializers()

    class Meta:
        model = Rating
        fields = (
            "rating",
            "review",
            "users",
            "date",
            "places"
        )