
from rest_framework.permissions import IsAuthenticated
from ..models import Discount
from ..serializers.dicount import ListDiscountSerializers, CreateDiscountSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


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
