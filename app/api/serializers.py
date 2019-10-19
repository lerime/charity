from app.api.models import Student, Aphorism, Faq, ReportMessage, Question

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'gender', 'group', 'teacher')


class AphorismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aphorism
        fields = ('id', 'content', 'subtitle')


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'description', 'video_link', 'cover_photo_link', 'view_size')


class ReportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMessage
        fields = ('id', 'message')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer')
