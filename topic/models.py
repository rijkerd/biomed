from django.db import models

"""
 Refers to an area being discussed can also be referred to as subject.

 Example:
    - Module: Networking - ETT 01012
    - Topic : Introduction to networking
"""


class Topic(models.Model):
    id = models.BigAutoField(
        primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # files = models.ForeignKey(
    #     TopicFile, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
