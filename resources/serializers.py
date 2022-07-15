from rest_framework import serializers

from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='id')

    class Meta:
        model = Resource
        fields = "__all__"
