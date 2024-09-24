
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from app_tour.filters import DiscountFilter
from ..serializers.dicount import ListDiscountSerializers, CreateDiscountSerializers
from ..models import Discount


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = CreateDiscountSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DiscountFilter
    search_fields = ['place', 'description', 'discount_percentage', 'start_date', 'end_date']
    ordering_fields = ['place', 'discount_percentage']
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ListDiscountSerializers
        return CreateDiscountSerializers
    
    
class CreateDiscountView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = CreateDiscountSerializers
    permission_classes = [IsAuthenticated]


class ListDiscountView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = ListDiscountSerializers
    permission_classes = [IsAuthenticated]
    

class RetrieveDiscountView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = ListDiscountSerializers
    permission_classes = [IsAuthenticated]


class DeleteDiscountView(DestroyAPIView):
    queryset = Discount.objects.all()
    permission_classes = [IsAuthenticated]


class UpdateDiscountView(UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = CreateDiscountSerializers
    permission_classes = [IsAuthenticated]
