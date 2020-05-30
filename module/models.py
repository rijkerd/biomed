from django.db import models


course_type = ('Core', 'Fundamental')


class Module(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # type = models.CharField(
    #     choices=course_type, default='Fundamental', max_length=100,)

    def __str__(self):
        return self.name


class Topic(models.Model):
    id = models.BigAutoField(
        primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # files = models.ForeignKey(
    #     TopicFile, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Resource(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='resources')
    name = models.CharField(default='Test', max_length=100)
    url = models.FileField(upload_to='files', blank=False)

    def __str__(self):
        return self.name
