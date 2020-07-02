from rest_framework.viewsets import ModelViewSet

from .models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
