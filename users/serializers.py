from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(
    #     validators=[UniqueValidator(queryset=User.objects.all())])
    # email = serializers.EmailField(required=True, validators=[
    #                                UniqueValidator(queryset=User.objects.all())])
    # password = serializers.CharField(min_length=8)

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         validated_data['username'], validated_data['email'], validated_data['password'])
    #     return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'user_permissions', 'is_staff', 'date_joined',
                  'last_login')
