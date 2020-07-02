from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ResourceViewSet

resource_list = ResourceViewSet.as_view({
    'get': 'list',
})

resource_detail = ResourceViewSet.as_view({
    'get': 'retrieve'
})


router = DefaultRouter()
router.register(r'resources', ResourceViewSet, basename='resource')
urlpatterns = router.urls
