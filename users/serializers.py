from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'groups', 'user_permissions', 'is_staff', 'date_joined',
                  'last_login',)
