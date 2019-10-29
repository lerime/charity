from django.db import models


class Aphorism(models.Model):
    content = models.CharField(max_length=500, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
