from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('/', include('module.urls')),
    path('/', include('topic.urls')),
    path('/', include('users.urls')),
]
