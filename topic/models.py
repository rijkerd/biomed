import uuid
from django.db import models
from module.models import Module

"""
 Refers to an area being discussed can also be referred to as subject.

 Example:
    - Module: Networking - ETT 01012
    - Topic : Introduction to networking
"""


class Topic(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    module = models.ForeignKey(
        Module, related_name='topics', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # files = models.ForeignKey(
    #     TopicFile, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
