from rest_framework import serializers

from app.report.models import Report, ReportMessage


class ReportSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.pray = validated_data.get('pray', 0)
        instance.epistle = validated_data.get('epistle', 0)
        instance.quran = validated_data.get('quran', 0)
        instance.jawshan = validated_data.get('jawshan', 0)
        instance.super_pray = validated_data.get('super_pray', 0)
        instance.fasting = validated_data.get('fasting', 0)
        instance.night_pray = validated_data.get('night_pray', 0)
        instance.evening_super_pray = validated_data.get('evening_super_pray', 0)
        instance.checked = True
        instance.save()
        return instance

    class Meta:
        model = Report
        exclude = ('group', )
        extra_kwargs = {'student_id': {'required': True}}


class ReportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMessage
        fields = ('id', 'message')
