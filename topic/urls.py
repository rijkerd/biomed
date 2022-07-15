from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ShowTopicResources, TopicViewSet

topic_list = TopicViewSet.as_view({
    'get': 'list',
})

topic_detail = TopicViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')

urlpatterns = router.urls

# urlpatterns = [
#     path('topics/<id>/', ShowTopicResources.as_view(), name='topic-details')
# ]
