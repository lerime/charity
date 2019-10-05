from django.db.models import Q

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from app.api.models import Student


def is_student_exist(data):
    phone_number = data.get('phone_number')
    student = Student.objects.filter(phone_number=phone_number)

    if student:
        return True
    return False

def create_student(data):
    student = Student()
    student.fullname = data.get('fullname')
    student.phone_number = data.get('phone_number')
    student.email = data.get('email')
    student.gender = data.get('gender', 'F')
    student.password = data.get('password')

    student.save()


def is_login_data_valid(data):
    fullname = data.get('fullname')
    phone_number = data.get('phone_number')
    username = data.get('username')
    password = data.get('password')

    if phone_number in ['', None]:
        raise ValidationError('Phone number is required')
    if fullname in ['', None]:
        raise ValidationError('Full name is required')
    if password in ['', None]:
        raise ValidationError('Password name is required')

    return True


