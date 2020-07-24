from rest_framework import serializers
from .models import Topic
from resources.serializers import ResourceSerializer


class TopicSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='id')
    # resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = "__all__"
