from django.conf import settings
from django.utils import timezone

from app.report.models import Report

DEFAULT_REPORT_COUNT = getattr(settings, 'DEFAULT_REPORT_COUNT', 30)


def create_report(group, report_count=DEFAULT_REPORT_COUNT):
    # objs = (Entry(headline='Test %s' % i) for i in range(1000))
    report_obj_list = []
    day = timezone.now()
    for student in group.students.all():

        for i in range(report_count):
            report_obj_list.append(Report(student_id=student.id, group_id=group.id, day=day))
            day += timezone.timedelta(days=1)
    created_objs = Report.objects.bulk_create(report_obj_list)
    #todo if not success raise error
    return created_objs
