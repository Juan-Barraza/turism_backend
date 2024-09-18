from rest_framework import serializers
from ..models import Place
#from .serializers import Category2Serializer, User2Serializer


class ListPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "category",
            "description",
            "latitude",
            "longitude",
            "price",
            "opening_hours",
            "tags",
            "picture"
        )

class CreatePlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = (
            "name",
            "category",
            "description",
            "latitude",
            "longitude",
            "price",
            "opening_hours",
            "tags"
            "picture"
        )

