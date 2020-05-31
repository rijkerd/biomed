from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Module, Topic
from .serializers import ModuleSerializer, TopicSerializer


class ModuleList(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TopicListJson(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'topic/show.html'

    def get(self, request):
        topic = Topic.objects.all()
        serializer = TopicSerializer(topic, many=True)
        return Response({'topics': serializer.data})


class TopicDetails(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
