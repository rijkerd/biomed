
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'username', 'password','user_type')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'user_permissions', 'is_staff', 'date_joined',
                  'last_login')
        extra_kwargs = {'password': {'write_only': True}}
