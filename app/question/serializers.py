from rest_framework import serializers

from app.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer')
