from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from app_tour.filters import PlaceFilter
from ..serializers.place import ListPlaceSerializer, CreatePlaceSerializer
from ..models import Place

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = CreatePlaceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PlaceFilter
    search_fields = ['name', 'price', 'description', 'tags']
    ordering_fields = ['price', 'name']
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ListPlaceSerializer
        return CreatePlaceSerializer


class CreatePlaceView(CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = CreatePlaceSerializer
    permission_classes = [IsAuthenticated]


class ListPlaceView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ListPlaceSerializer
    permission_classes = [IsAuthenticated]
    

class RetrievePlaceView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = ListPlaceSerializer
    permission_classes = [IsAuthenticated]


class DeletePlaceView(DestroyAPIView):
    queryset = Place.objects.all()
    permission_classes = [IsAuthenticated]


class UpdatePlaceView(UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = CreatePlaceSerializer
    permission_classes = [IsAuthenticated]

