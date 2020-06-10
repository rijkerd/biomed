from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Topic
from .serializers import TopicSerializer


class TopicViewSet(ModelViewSet):
    lookup_field = 'id'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
