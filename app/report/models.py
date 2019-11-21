from django.db import models


class Report(models.Model):
    student_id = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey('account.Group', on_delete=models.CASCADE, null=True, blank=True)
    pray = models.IntegerField(default=-1)
    epistle = models.IntegerField(default=-1)
    quran = models.IntegerField(default=-1)
    jawshan = models.IntegerField(default=-1)
    super_pray = models.IntegerField(default=-1)
    fasting = models.IntegerField(default=-1)
    night_pray = models.IntegerField(default=-1)
    evening_super_pray = models.IntegerField(default=-1)
    checked = models.BooleanField(default=False)
    day = models.DateField(null=True, blank=True)


class ReportMessage(models.Model):
    message = models.CharField(max_length=255, null=True, blank=True)
