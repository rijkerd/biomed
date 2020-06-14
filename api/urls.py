from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path('/', include('module.urls')),
    path('/', include('topic.urls')),
    path('/biomed-openapi', get_schema_view(
        title="Biomed",
        description="Biomed openapi",
        version="0.1.0"
    ), name='biomed-openapi-schema'),
    path('/swagger-ui', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'biomed-openapi-schema'}
    ), name='swagger-ui'),
]
