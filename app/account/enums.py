from enum import Enum

from app.account.models import Student, Teacher, StudentAuthToken, TeacherAuthToken


class LoginEnum(Enum):
    default = Student
    student = Student
    teacher = Teacher


class TokenEnum(Enum):
    student = StudentAuthToken
    teacher = TeacherAuthToken
