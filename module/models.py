import uuid

from django.db import models

# from topic.models import Topic

course_type = [('C', 'Core'), ('F', 'Fundamental')]


# TODO: Module should have many topics
# TODO: Module should contain NTA Level ie NTA Level 4
# TODO: Module should contain credits
# TODO: Module need to be linked to a programme ie Diploma / Degree in Biomedical engineering

class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    category = models.CharField(
        choices=course_type, max_length=2, blank=False, default='C')
    code = models.CharField(max_length=10, blank=True, default='EBE-0101')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
