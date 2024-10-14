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
            "email",
            "picture",
            "location",
            "gender",
            "born_day",
        )
        extra_kwargs = {'password': {'write_only': True},
                        'is_admin': {'write_only': True}}
        


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "preferred_language",
            "is_vip",
            "preferences",
            "picture",
            "location",
            "gender",
            "born_day",
        )
    extra_kwargs = {'password': {'write_only': True},
                    'is_admin': {'write_only': True},
                    'preferred_language': {'required': False},  
                    'is_vip': {'required': False},              
                    'preferences': {'required': False},
                    'picture': {'required': False},
                    'id': {'requiered': False}}

        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_admin = True  
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
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
            "email",
            "picture",
            "location",
            "gender",
            "born_day",
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  
            'username': {'required': False},
            'preferred_language': {'required': False},  
                    'is_vip': {'required': False},              
                    'preferences': {'required': False},
                    'picture': {'required': False},
                    'id': {'requiered': False}
  
        }
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['preferences'] = instance.preferences.split(',') if instance.preferences else []
        return data
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        preferences = validated_data.pop('preferences', None)
        if password:
            instance.set_password(password) 
        
        if preferences is not None:
            validated_data['preferences'] = ','.join(preferences)
            
        for attr, value in validated_data.items():
            if value != "":
                setattr(instance, attr, value)
        instance.save()
        return instance