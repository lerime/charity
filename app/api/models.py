from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Teacher(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)


class Course(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    quran = models.PositiveIntegerField()
    epistle = models.PositiveIntegerField()
    jawshan = models.PositiveIntegerField()
    extra = models.PositiveIntegerField()
    pray = models.PositiveIntegerField()
    min_point = models.IntegerField()
    description = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)


class Group(models.Model):
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE)
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    size = models.IntegerField()


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=128, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F', null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
