from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    pray = models.PositiveIntegerField(default=True)
    epistle = models.PositiveIntegerField(default=True)
    quran = models.PositiveIntegerField(default=True)
    jawshan = models.PositiveIntegerField(default=True)
    super_pray = models.PositiveIntegerField(default=True)
    fasting = models.PositiveIntegerField(default=True)
    night_pray = models.PositiveIntegerField(default=True)
    evening_super_pray = models.PositiveIntegerField(default=True)
    min_point = models.IntegerField(null=True, blank=True)
    image_link = models.CharField(max_length=255, null=True, blank=True)
