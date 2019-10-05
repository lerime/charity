from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins


from app.api.serializers import StudentSerializer
from app.api.helpers import is_student_exist, create_student, is_login_data_valid
from app.api.models import Student

class UserLoginApiView(APIView):
    serializer_class = StudentSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        if not is_login_data_valid(request.data):
            return Response({
                'error': True,
                'status_code': 400,
                'result': {}
            }, status=status.HTTP_400_BAD_REQUEST)
        student = get_object_or_404(Student, username=request.data.get('username'))
        serializer = self.serializer_class(student)

        return Response({
            'error': False,
            'status': '200',
            'result': serializer.data

        })


class StudentViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def create(self, request):

        data = request.data
        if is_student_exist(data):
            return Response({
                'error': False,
                'status': 400,
                'errors': "There is another user"
            }, status=status.HTTP_400_BAD_REQUEST)
        create_student(data)
        return Response({
            'error': False,
            'status': '200'
        })
