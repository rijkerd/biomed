import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO: Setup email verification
# TODO: Setup user roles and permissions IE: Student and Teacher permissions


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['last_login']

    def __str__(self):
        return self.email
