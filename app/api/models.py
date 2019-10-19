from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Teacher(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)


class Course(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    quran = models.PositiveIntegerField()
    epistle = models.PositiveIntegerField()
    jawshan = models.PositiveIntegerField()
    extra = models.PositiveIntegerField()
    pray = models.PositiveIntegerField()
    min_point = models.IntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)
    image_link = models.CharField(max_length=255, null=True, blank=True)


class Group(models.Model):
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE)
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
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


class Aphorism(models.Model):
    content = models.CharField(max_length=500, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)


class Question(models.Model):
    question = models.CharField(max_length=500, null=True, blank=True)
    optionA = models.CharField(max_length=255, null=True, blank=True)
    optionB = models.CharField(max_length=255, null=True, blank=True)
    optionC = models.CharField(max_length=255, null=True, blank=True)
    optionD = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, blank=True)


class Faq(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.CharField(max_length=255, null=True, blank=True)
    cover_photo_link = models.CharField(max_length=255, null=True, blank=True)
    view_size = models.CharField(max_length=255, null=True, blank=True)


class ReportMessage(models.Model):
    message = models.CharField(max_length=255, null=True, blank=True)


# class Report(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
#     group = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
#     quran = models.PositiveIntegerField()
#     epistle = models.PositiveIntegerField()
#     jawshan = models.PositiveIntegerField()
#     pray = models.PositiveIntegerField()
