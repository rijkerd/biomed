from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from .models import Topic
from .serializers import TopicSerializer


class TopicViewSet(ModelViewSet):
    lookup_field = 'id'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ShowTopicResources(GenericAPIView):
    lookup_field = 'id'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'topic/show.html'

    def get(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'topics': serializer.data})
