from rest_framework import serializers

from app.report.models import Report, ReportMessage


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        extra_kwargs = {'student_id': {'required': True}}


class ReportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMessage
        fields = ('id', 'message')
