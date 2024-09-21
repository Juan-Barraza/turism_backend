from rest_framework import serializers
from app_tour.models import Visit_history, Place
from .user import ListUserSerializers
from .place import ListPlaceSerializer

class ListVisitHistorySerializers(serializers.ModelSerializer):
    place = ListPlaceSerializer()
    user = ListUserSerializers()

    class Meta:
        model = Visit_history
        fields = (
            "id",
            "visit_date",
            "times_visited",
            "user",
            "place"
        )

class CreateVisitHistorySerializers(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())
    class Meta:
        model = Visit_history
        fields = (
            "place",
        )