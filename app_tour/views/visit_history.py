from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from app_tour.models import Visit_history, Place
from app_tour.filters import VisitHistoryFilter
from ..serializers.visit_history import ListVisitHistorySerializers, CreateVisitHistorySerializers


class VisitHistoryViewSet(ModelViewSet):
    queryset = Visit_history.objects.all()
    serializer_class = CreateVisitHistorySerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = VisitHistoryFilter
    search_fields = ['place__name', 'user__first_name', 'visit_date']
    ordering_fields = ['visit_date', 'place__name']
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrive":
            return ListVisitHistorySerializers
        return CreateVisitHistorySerializers
    
    def perform_create(self, serializer):
        user = self.request.user
        place_id = self.request.data.get('place')
        place = get_object_or_404(Place, id=place_id)
        serializer.save(user=user, place=place)
    
    
class CreateVisitHistoryView(CreateAPIView):
    queryset = Visit_history.objects.all()
    serializer_class = CreateVisitHistorySerializers
    permission_classes = [IsAuthenticated]


class ListVisitHistoryView(ListAPIView):
    queryset = Visit_history.objects.all()
    serializer_class = ListVisitHistorySerializers
    permission_classes = [IsAuthenticated]
    

class RetrieveVisitHistoryView(RetrieveAPIView):
    queryset = Visit_history.objects.all()
    serializer_class = ListVisitHistorySerializers
    permission_classes = [IsAuthenticated]


class DeleteVisitHistoryView(DestroyAPIView):
    queryset = Visit_history.objects.all()
    permission_classes = [IsAuthenticated]


class UpdateVisitHistoryView(UpdateAPIView):
    queryset = Visit_history.objects.all()
    serializer_class = CreateVisitHistorySerializers
    permission_classes = [IsAuthenticated]

