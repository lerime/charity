from django.db import models


class Report(models.Model):
    student_id = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey('account.Group', on_delete=models.CASCADE, null=True, blank=True)
    pray = models.PositiveIntegerField(default=0)
    epistle = models.PositiveIntegerField(default=0)
    quran = models.PositiveIntegerField(default=0)
    jawshan = models.PositiveIntegerField(default=0)
    super_pray = models.PositiveIntegerField(default=0)
    fasting = models.PositiveIntegerField(default=0)
    night_pray = models.PositiveIntegerField(default=0)
    evenint_super_pray = models.PositiveIntegerField(default=0)
    checked = models.BooleanField(default=False)
    day = models.DateTimeField(null=True, blank=True)


class ReportMessage(models.Model):
    message = models.CharField(max_length=255, null=True, blank=True)
