from rest_framework import serializers

from app.account.models import Group
from app.account.models import Student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'gender', 'group', 'teacher')


class StudentLoginSerializer(StudentSerializer):
    token = serializers.CharField()
    course_id = serializers.CharField()

    class Meta(StudentSerializer.Meta):
        fields = ('id', 'token', 'fullname', 'group_id', 'course_id')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        #todo add controls
        return attrs

    def create(self, validated_data):
        #
        validated_data.pop('student_ids')

        return Group.objects.create(**validated_data)

    class Meta:
        model = Group
        fields = '__all__'
