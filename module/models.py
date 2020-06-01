from django.db import models
from topic.models import Topic

"""
 Is representation of a subject take by an individual/student on a 
 particular programme.

 - Attached to a particalar NTA Level eg. NTA 5

 example: Radio Transmission ETT-01025

"""
course_type = ('Core', 'Fundamental')


class Module(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=30, blank=True, default='EBE 0101')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # type = models.CharField(
    #     choices=course_type, default='Fundamental', max_length=100,)

    def __str__(self):
        return self.name


class Resource(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='resources')
    name = models.CharField(default='Test', max_length=100)
    url = models.FileField(upload_to='files', blank=False)

    def __str__(self):
        return self.name
