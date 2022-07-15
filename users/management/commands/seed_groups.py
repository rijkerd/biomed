from unicodedata import name

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from module.models import Module
from resources.models import Resource
from topic.models import Topic


class Command(BaseCommand):
    help = 'Seed Groups for the System'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding ....')
        seed_teacher_group(self)
        seed_student_group(self)
        # seed_test(self)
        self.stdout.write(self.style.SUCCESS('Seed Completed'))


def seed_teacher_group(self):
        teacher = Group.objects.filter(name="teacher")
        
        if teacher.exists():
            self.stdout.write('Teacher Group all ready exists')
        else:
            topics_content = ContentType.objects.get_for_model(Topic)
            resource_content = ContentType.objects.get_for_model(Resource)
            topic_permissions = Permission.objects.filter(content_type=topics_content)
            resource_permissions = Permission.objects.filter(content_type=resource_content)
            teacher_group,_ = Group.objects.get_or_create(name='teacher')
            teacher_group.permissions.set([*topic_permissions,*resource_permissions]);
            self.stdout.write(self.style.SUCCESS('Seed Teacher Completed'))

def seed_student_group(self):
        student = Group.objects.filter(name="student")
        
        if student.exists():
            self.stdout.write('Student Group all ready exists')
        else:
            topics_content = ContentType.objects.get_for_model(Topic)
            resource_content = ContentType.objects.get_for_model(Resource)
            module_content =  ContentType.objects.get_for_model(Module)
            topic_permissions = Permission.objects.get(content_type=topics_content,codename="view_topic")
            resource_permissions = Permission.objects.get(content_type=resource_content,codename="view_resource")
            module_permission = Permission.objects.get(content_type=module_content,codename="view_module")
            student_group,_ = Group.objects.get_or_create(name='student')
            student_group.permissions.set([topic_permissions,resource_permissions,module_permission]);
            self.stdout.write(self.style.SUCCESS('Seed Student Completed'))
