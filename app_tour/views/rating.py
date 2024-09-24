
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404
from app_tour.filters import RatingFilter
from ..serializers.rating import ListRatingSerializers, CreateRatingSerializers
from app_tour.models import Rating, Place


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RatingFilter
    search_fields = ['place', 'user', 'rating', 'review', 'date']
    ordering_fields = ['place', 'rating']
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ListRatingSerializers
        return CreateRatingSerializers
    
    def perform_create(self, serializer):
        user = self.request.user
        place_id = self.request.data.get('place')
        place = get_object_or_404(Place, id=place_id)
        serializer.save(user=user, place=place)
        
class CreateRatingView(CreateAPIView):
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

