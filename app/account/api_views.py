from django.contrib.auth import login as auth_login
from django.shortcuts import get_object_or_404
from rest_framework import status, exceptions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.account.enums import LoginEnum, TokenEnum
from app.account.helpers import is_student_exist, create_student, validate_login_data
from app.account.models import Student, Group
from app.account.serializers import StudentSerializer, GroupSerializer


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


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.prefetch_related('groups').all()  # todo add prefetch related configs
