from django.contrib.auth.hashers import make_password

from rest_framework.exceptions import ValidationError

from app.account.models import Student


def is_student_exist(data):
    username = data.get('username')
    student = Student.objects.filter(username=username)

    if student:
        return True
    return False


def create_student(data):
    student = Student()
    student.username = data.get('username')
    student.phone_number = data.get('phone_number')
    student.email = data.get('email')
    student.gender = data.get('gender', 'F')
    student.password = make_password(data.get('password'))

    student.save()


def validate_login_data(data):
    username = data.get('username')
    password = data.get('password')

    if username in ['', None]:
        raise ValidationError('Username is required')
    if password in ['', None]:
        raise ValidationError('Password is required')
