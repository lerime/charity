from rest_framework import viewsets, mixins
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from app.report.models import Report, ReportMessage
from app.report.serializers import ReportSerializer, ReportMessageSerializer


class ReportViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request):
        report = get_object_or_404(Report, student_id=request.GET.get('student_id'))
        data = self.serializer_class(instance=report).data
        return Response(data)

class ReportMessageViewSet(viewsets.ModelViewSet):
    queryset = ReportMessage.objects.all()
    serializer_class = ReportMessageSerializer
