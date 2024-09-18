from rest_framework import serializers
from ..models import Visit_history
from serializers import ListPlaceSerializer, ListUserSerializers

class ListVisitHistorySerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()
    users = ListUserSerializers()

    class Meta:
        model = Visit_history
        fields = (
            "id",
            "visit_date",
            "times_visited",
            "users",
            "places"
        )

class CreateVisitHistorySerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()
    users = ListUserSerializers()

    class Meta:
        model = Visit_history
        fields = (
            "visit_date",
            "times_visited",
            "users",
            "places"
        )
