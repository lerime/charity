import datetime

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from app.report.models import Report, ReportMessage
from app.report.serializers import ReportSerializer, ReportMessageSerializer

date_format = '%Y-%m-%d'


class ReportViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request):
        student_id = request.query_params.get('student_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if end_date is None:
            date = datetime.datetime.strptime(start_date, date_format)
            end_date = date.replace(hour=23, minute=59, second=59)
        queryset = self.queryset.filter(student_id=student_id,
                                        day__gte=start_date,
                                        day__lte=end_date)

        data = self.serializer_class(instance=queryset, many=True).data
        return Response(data)

    def put(self, request, *args, **kwargs):
        data = request.data
        date = data.get('day') #add control
        report = self.queryset.filter(student_id=data.get('student_id'),
                                      day=date).first()
        serializer = self.serializer_class(report, data=data)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        return Response(serializer.data)


class ReportMessageViewSet(viewsets.ModelViewSet):
    queryset = ReportMessage.objects.all()
    serializer_class = ReportMessageSerializer
