from app.api.models import Student

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'gender', 'group', 'teacher')
