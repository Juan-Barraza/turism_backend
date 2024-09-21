from django.db.models import Avg
from rest_framework import serializers

from app_tour.models import Place, Rating, Visit_history


class ListPlaceSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    number_of_ratings = serializers.SerializerMethodField()
    times_visited = serializers.SerializerMethodField()
    
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
            "picture",
            "average_rating",
            "number_of_ratings",
            "times_visited",
        )
        
    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(place_id=obj.id)
        avg_rating = (ratings.aggregate(Avg("rating")))["rating__avg"]

        if avg_rating is not None:
            return round(avg_rating, 2)

        return None
    
    def get_number_of_ratings(self, obj):
        ratings = Rating.objects.filter(place_id=obj.id)
        return ratings.count()
    
    def get_times_visited(self, obj):
        visited = Visit_history.objects.filter(place_id=obj.id)
        return visited.count()


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
            "tags",
            "picture",
        )

