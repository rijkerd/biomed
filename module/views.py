from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import Module, Topic
from .serializers import ModuleSerializer, TopicSerializer


class ModuleList(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TopicList(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetails(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
