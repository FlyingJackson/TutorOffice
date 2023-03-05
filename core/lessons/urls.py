from django.urls import path, include
from rest_framework import routers
from .viewsets import SubjectViewSet, LessonViewSet


router = routers.DefaultRouter()
router.register(r"subjects", SubjectViewSet, basename="subjects")
router.register(r"lessons", LessonViewSet, basename="lessons")


urlpatterns = [
    path("", include(router.urls)),
]