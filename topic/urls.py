from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet

topic_list = TopicViewSet.as_view({
    'get': 'list',
})

topic_detail = TopicViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')

urlpatterns = router.urls
