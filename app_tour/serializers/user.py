from rest_framework import serializers
from ..models import User

class ListUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "preferred_language",
            "is_vip",
            "preferences",
            "email"
        )
        extra_kwargs = {'password': {'write_only': True},
                        'is_admin': {'write_only': True},
                        'preferred_language': {'required': False},  
                        'is_vip': {'required': False},              
                        'preferences': {'required': False}}
        


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "preferred_language",
            "is_vip",
            "preferences"
        )
    extra_kwargs = {'password': {'write_only': True},
                    'is_admin': {'write_only': True}}

        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_admin = True  
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "preferred_language",
            "is_vip",
            "preferences"
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  
            'username': {'required': False},  
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password) 
        for attr, value in validated_data.items():
            if value != "":
                setattr(instance, attr, value)

        instance.save()
        return instance