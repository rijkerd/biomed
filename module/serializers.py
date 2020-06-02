from rest_framework import serializers
from topic.serializers import TopicSerializer
from .models import Module


class ModuleSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = "__all__"
