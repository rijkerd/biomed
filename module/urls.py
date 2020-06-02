from django.urls import path
from .views import ModuleList
from django.views.generic.base import TemplateView

from topic.views import TopicList, TopicDetails, TopicListJson


class TestTemplate(TemplateView):
    template_name = "home.html"


urlpatterns = [
    path('', TestTemplate.as_view()),
    path('modules', ModuleList.as_view(), name='module-list'),
    path('topics', TopicListJson.as_view(), name='topic-list'),
    path('topics/<id>', TopicDetails.as_view(), name='topic-detail'),
]
