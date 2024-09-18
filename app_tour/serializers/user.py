from rest_framework import serializers
from ..models import User
from serializers import ListPlaceSerializer, ListRatingSerializers

class ListUserSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()
    users = ListRatingSerializers

    class Meta:
        model = User
        fields = (
            "id",
            "preferred_language",
            "is_vip",
            "preferences"
        )

class CreateUserSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()

    class Meta:
        model = User
        fields = (
            "preferred_language",
            "is_vip",
            "preferences"
        )