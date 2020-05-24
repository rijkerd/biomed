from django.urls import path
from .views import ModuleList, TopicList, TopicDetails, TopicFileList


urlpatterns = [
    path('modules', ModuleList.as_view(), name='module-list'),
    path('topics', TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>', TopicDetails.as_view(), name='topic-detail'),
    path('topics/<int:pk>/topicfiles',
         TopicFileList.as_view(), name='topicfiles-detail')
]
