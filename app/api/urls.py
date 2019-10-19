from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.api_views import StudentViewSet, UserLoginApiView, AphorismViewSet, FaqViewSet, ReportMessageViewSet, \
    QuestionViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'aphorism', AphorismViewSet, basename='aphorism')
router.register(r'faq', FaqViewSet, basename='faq')
router.register(r'report-message', ReportMessageViewSet, basename='report_message')
router.register(r'question', QuestionViewSet, basename='question')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]