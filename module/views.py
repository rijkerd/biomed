from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Module
from .serializers import ModuleSerializer


class ModuleViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
