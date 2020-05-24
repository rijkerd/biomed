from django.contrib import admin
from .models import Module, Topic, TopicFile

# Register your models here.
admin.site.register(Module)
admin.site.register(Topic)
admin.site.register(TopicFile)
