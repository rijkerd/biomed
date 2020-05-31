from django.urls import path
from .views import ModuleList, TopicList, TopicDetails, TopicListJson
from django.views.generic.base import TemplateView


class TestTemplate(TemplateView):
    template_name = "home.html"


urlpatterns = [
    path('', TestTemplate.as_view()),
    path('modules', ModuleList.as_view(), name='module-list'),
    path('topics', TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>', TopicDetails.as_view(), name='topic-detail'),
]
