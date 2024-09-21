from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from ..serializers.user import CreateUserSerializers, ListUserSerializers, UpdateUserSerializer
from ..models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializers
    
    @permission_classes([IsAuthenticated])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @permission_classes([IsAuthenticated])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @permission_classes([IsAuthenticated])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @permission_classes([IsAuthenticated])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @permission_classes([IsAuthenticated])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ListUserSerializers
        return CreateUserSerializers
    
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