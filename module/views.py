from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from .models import Module
from .serializers import ModuleSerializer


class ModuleViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleList(GenericAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ListAll(ModuleList):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'module_list.html'

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({'modules': serializer.data})


class ModuleTopic(ModuleList):
    lookup_field = "id"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'topic/topic_list.html'

    def get(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response({'module': serializer.data})
