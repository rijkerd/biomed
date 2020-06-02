from rest_framework import serializers
from .models import Topic
# from module.serializers import ModuleSerializer


class TopicSerializer(serializers.ModelSerializer):
    # resources = ResourceSerializer(
    #     many=True, read_only=True)
    module = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')

    class Meta:
        model = Topic
        fields = "__all__"

# class ResourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resource
#         fields = ('id', 'name', 'url')
