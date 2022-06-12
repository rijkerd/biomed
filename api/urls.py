from django.urls import include, path

urlpatterns = [
    path('/', include('module.urls')),
    path('/', include('topic.urls')),
    path('/', include('users.urls')),
    path('/', include('resources.urls')),
    path('/', include('users.urls')),
]
