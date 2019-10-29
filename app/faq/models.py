from django.db import models


class Faq(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.CharField(max_length=255, null=True, blank=True)
    cover_photo_link = models.CharField(max_length=255, null=True, blank=True)
    view_size = models.CharField(max_length=255, null=True, blank=True)
