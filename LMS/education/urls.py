from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter
from education.views import LessonViewSet, CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetriveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

from django.urls import path

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path("lesson/create", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>", LessonRetriveAPIView.as_view(), name="lesson-get"),
    path("lesson/update/<int:pk>", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="lesson-delete"),
]+router.urls
