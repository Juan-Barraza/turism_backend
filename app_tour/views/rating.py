from rest_framework.permissions import IsAuthenticated
from ..models import Rating
from ..serializers.rating import ListRatingSerializers, CreateRatingSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

class CreateDiscountView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializers
    permission_classes = [IsAuthenticated]


class ListRatingView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = ListRatingSerializers
    permission_classes = [IsAuthenticated]
    

class RetrieveRatingView(RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = ListRatingSerializers
    permission_classes = [IsAuthenticated]


class DeleteRatingView(DestroyAPIView):
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]


class UpdateRatingView(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializers
    permission_classes = [IsAuthenticated]

