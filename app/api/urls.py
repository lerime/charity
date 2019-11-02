from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.account.api_views import StudentViewSet, TeacherViewSet, UserLoginApiView, GroupViewSet
from app.aphorism.api_views import AphorismViewSet
from app.faq.api_views import FaqViewSet
from app.question.api_views import QuestionViewSet
from app.report.api_views import ReportMessageViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'aphorism', AphorismViewSet, basename='aphorism')
router.register(r'faq', FaqViewSet, basename='faq')
router.register(r'report-message', ReportMessageViewSet, basename='report_message')
router.register(r'question', QuestionViewSet, basename='question')

urlpatterns = [
    path('login/<str:user_type>', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
