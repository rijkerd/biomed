from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ResourceViewSet, download_from_s3

resource_list = ResourceViewSet.as_view({
    'get': 'list',
})

resource_detail = ResourceViewSet.as_view({
    'get': 'retrieve'
})


router = DefaultRouter()
router.register(r'resources', ResourceViewSet, basename='resource')
urlpatterns = [
    url(r'^resources/download_file/(?P<id>[^/.]+)/$', download_from_s3)
]

urlpatterns += router.urls

print(urlpatterns)
