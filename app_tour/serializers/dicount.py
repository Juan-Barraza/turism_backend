from rest_framework import serializers
from ..models import Discount
from .place import ListPlaceSerializer

class ListDiscountSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()

    class Meta:
        model = Discount
        fields = (
            "id",
            "description",
            "discount_percentage",
            "start_date",
            "end_date",
            "places"
        )

class CreateDiscountSerializers(serializers.ModelSerializer):
    places = ListPlaceSerializer()

    class Meta:
        model = Discount
        fields = (
            "description",
            "discount_percentage",
            "start_date",
            "end_date",
            "places"
        )