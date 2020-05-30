from django.urls import path
from .views import ModuleList, TopicList, TopicDetails


urlpatterns = [
    path('modules', ModuleList.as_view(), name='module-list'),
    path('topics', TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>', TopicDetails.as_view(), name='topic-detail'),
]
