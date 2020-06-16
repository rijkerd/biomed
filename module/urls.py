from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, ListAll, ModuleTopic

module_list = ModuleViewSet.as_view({
    'get': 'list',
})

module_detail = ModuleViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'modules', ModuleViewSet, basename='module')
urlpatterns = router.urls

# urlpatterns = [
#     path('modules/', ListAll.as_view(), name='modules-lists'),
#     path('modules/<id>', ModuleTopic.as_view(), name='modules-details'),
# ]
