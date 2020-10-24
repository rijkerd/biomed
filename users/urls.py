
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


users_list = UserViewSet.as_view({
    'get': 'list',
})

users_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
# urlpatterns = [
#     url(r'users^$', UserCreate.as_view(), name='users-create'),
# ]
