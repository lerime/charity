from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

from app.account.enums import LoginEnum
from app.account.models import Student, Teacher


def is_student_exist(data):
    username = data.get('username')
    student = Student.objects.filter(username=username)

    if student:
        return True
    return False


def is_user_exist(user_type, data):
    model = LoginEnum[user_type].value if user_type else LoginEnum.default.value
    user = model.objects.filter(username=data.get('username'))
    if user:
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


def create_teacher(data):
    teacher = Teacher()
    teacher.username = data.get('username')
    teacher.phone_number = data.get('phone_number')
    teacher.email = data.get('email')
    teacher.gender = data.get('gender', 'F')
    teacher.password = make_password(data.get('password'))

    teacher.save()


def validate_login_data(data):
    username = data.get('username')
    password = data.get('password')

    if username in ['', None]:
        raise ValidationError('Username is required')
    if password in ['', None]:
        raise ValidationError('Password is required')


def set_users_group(student_id_list, group_id):
    for student_id in student_id_list:
        try:
            student = Student.objects.filter(id=student_id)
            student = student.first()
            student.group_id = group_id
            student.save()
        except Student.DoesNotExist as e:
            pass
