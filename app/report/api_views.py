from rest_framework import viewsets

from app.report.models import Report, ReportMessage
from app.report.serializers import ReportSerializer, ReportMessageSerializer

#todo sendDailyReport api , checkDailyReport api
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    


class ReportMessageViewSet(viewsets.ModelViewSet):
    queryset = ReportMessage.objects.all()
    serializer_class = ReportMessageSerializer
