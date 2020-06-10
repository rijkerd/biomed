from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet

module_list = ModuleViewSet.as_view({
    'get': 'list',
})

module_detail = ModuleViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')

urlpatterns = router.urls
