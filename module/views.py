from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Module
from .serializers import ModuleSerializer


class ModuleList(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
