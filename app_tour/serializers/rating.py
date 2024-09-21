from rest_framework import serializers
from app_tour.models import Rating, Place
from .user import ListUserSerializers
from .place import ListPlaceSerializer

class ListRatingSerializers(serializers.ModelSerializer):
    place = ListPlaceSerializer()
    user = ListUserSerializers()
    class Meta:
        model = Rating
        fields = (
            "id",
            "rating",
            "review",
            "user",
            "date",
            "place"
        )

class CreateRatingSerializers(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())

    class Meta:
        model = Rating
        fields = (
            "rating",
            "review",
            "date",
            "place",
        )