from rest_framework import serializers
from .models import Module, Topic, TopicFile


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name', 'description']


class TopicFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopicFile
        fields = '__all__'


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    # resources = serializers.HyperlinkedModelSerializer(many=True,view_name)
    class Meta:
        model = Topic
        fields = ['name', 'description', 'topic_id']
