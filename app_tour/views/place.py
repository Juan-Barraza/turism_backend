from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from ..serializers.place import ListPlaceSerializer, CreatePlaceSerializer
from ..models import Place


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = CreatePlaceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrive":
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

