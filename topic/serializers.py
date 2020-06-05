from rest_framework import serializers
from .models import Topic, Resource
# from module.serializers import ModuleSerializer


class ResourceSerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')

    class Meta:
        model = Resource
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = "__all__"
