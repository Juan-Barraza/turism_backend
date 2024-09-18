from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from ..models import User
from ..serializers.user import CreateUserSerializers, ListUserSerializers, UpdateUserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializers
    
class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializers
    permission_classes = [IsAuthenticated]
    
class RetriverUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializers
    permission_classes = [IsAuthenticated]

class DeleteUserView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]