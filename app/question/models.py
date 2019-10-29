from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=500, null=True, blank=True)
    optionA = models.CharField(max_length=255, null=True, blank=True)
    optionB = models.CharField(max_length=255, null=True, blank=True)
    optionC = models.CharField(max_length=255, null=True, blank=True)
    optionD = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, blank=True)
