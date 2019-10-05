from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.api_views import StudentViewSet, UserLoginApiView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]