import uuid
from django.db import models
from topic.models import Topic


class Resource(models.Model):
    """
    Refers to files that are provide with reference to a particular topic can be tutorials video, notes.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, default='default')
    description = models.CharField(
        max_length=200, blank=False, default='Not set')
    location = models.FileField(upload_to='resources', blank=False)
    topic = models.ForeignKey(
        Topic, related_name='resources', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_file_location(self):
        return str(self.location)
