
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status
from ..models import Rating
from rest_framework.response import Response
from ..serializers.rating import ListRatingSerializers, CreateRatingSerializers
from rest_framework.views import APIView


@permission_classes([IsAuthenticated])
class DiscountView(APIView):
    
    def post(self, request):
        serializer = CreateRatingSerializers(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        rating = Rating.objects.all()
        serializer = ListRatingSerializers(rating, many=True)
        
        if rating is None:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)