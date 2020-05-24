from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import Module, Topic, TopicFile
from .serializers import ModuleSerializer, TopicSerializer, TopicFileSerializer


class ModuleList(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TopicFileList(ListCreateAPIView):
    queryset = TopicFile.objects.all(),
    serializer_class = TopicFileSerializer


class TopicList(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetails(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
