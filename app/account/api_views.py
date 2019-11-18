from django.contrib.auth import login as auth_login
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import status, exceptions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.account.enums import LoginEnum, TokenEnum
from app.account.helpers import is_user_exist, create_teacher, create_student, validate_login_data, set_users_group
from app.account.models import Student, Group, Teacher
from app.account.serializers import StudentSerializer, GroupSerializer, TeacherSerializer
from app.report.helpers import create_report


class UserLoginApiView(APIView):
    serializer_class = StudentSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, user_type=None):
        validate_login_data(request.data)

        model = LoginEnum[user_type].value if user_type else LoginEnum.default.value
        user = get_object_or_404(model, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            raise exceptions.AuthenticationFailed()
        auth_login(request, user)
        token = generate_token(
            user=user, user_type=user_type, token_model=TokenEnum[user_type].value)

        return Response({'user_id': user.pk, 'token': token.key})


def generate_token(user, user_type, token_model=Token):
    token, created = token_model.objects.get_or_create(user=user)
    return token


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def create(self, request, **kwargs):
        data = request.data
        if is_user_exist('student', data):
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


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        if is_user_exist('teacher', data):
            return Response({
                'error': False,
                'status': 400,
                'errors': "There is another user"
            }, status=status.HTTP_400_BAD_REQUEST)
        create_teacher(data)
        return Response({
            'error': False,
            'status': '200'
        })


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.prefetch_related('groups').all()  # todo add prefetch related configs

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=False)
            group = serializer.save(**data)
            set_users_group(data.get('student_ids'), group.id)
            create_report(group)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            pass
