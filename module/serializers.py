from rest_framework import serializers
from .models import Module, Topic, Resource


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name', 'description']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'url')


class TopicSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(
        many=True, read_only=True)

    class Meta:
        model = Topic
        # fields = ['name', 'description', 'topic_id', 'resources']
        fields = "__all__"
