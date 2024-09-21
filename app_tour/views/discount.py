
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from ..serializers.dicount import ListDiscountSerializers, CreateDiscountSerializers
from ..models import Discount


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = CreateDiscountSerializers
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
