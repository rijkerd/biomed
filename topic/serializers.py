from rest_framework import serializers

from resources.serializers import ResourceSerializer

from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='id')
    # resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = "__all__"
