from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
# class UserCreate(APIView):
#     """
#     Creates the user.
#     """

#     def post(self, request, format='json'):
#         return Response('hello')
