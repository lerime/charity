from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    USERNAME_FIELD = 'username'

    fullname = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F', null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Teacher(User):
    group_size = models.PositiveIntegerField(default=0)


class Student(User):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True, related_name="students")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True, related_name='groups')


class Group(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    course = models.OneToOneField('api.Course', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    size = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


class StudentAuthToken(Token):
    user = models.OneToOneField(
        Student, related_name='stu_auth_token',
        on_delete=models.CASCADE
    )


class TeacherAuthToken(Token):
    user = models.OneToOneField(
        Teacher, related_name='tch_auth_token',
        on_delete=models.CASCADE
    )
