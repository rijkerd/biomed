import email
import uuid

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.dispatch import receiver

# TODO: Setup email verification

USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'secretary'),
      (4, 'supervisor'),
      (5, 'admin'),
  )

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.PositiveBigIntegerField(choices=USER_TYPE_CHOICES,default=1)

    class Meta:
        ordering = ['last_login']

    def __str__(self):
        return self.email

@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        new_user = User.objects.get(email=instance)
        user_groud_id =USER_TYPE_CHOICES[new_user.user_type-1]
        user_group = Group.objects.get(name=user_groud_id[1])
        new_user.groups.add(user_group)
        new_user.user_permissions.add(*user_group.permissions.all())
        new_user.save()
        