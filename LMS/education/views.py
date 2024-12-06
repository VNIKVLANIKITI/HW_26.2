from rest_framework import viewsets, generics
from education.serializers import LessonSerializer, CourseSerializer
from education.models import lesson, course
from rest_framework.permissions import IsAuthenticated
from education.permissions import IsCurator
from education.paginators import lessonPaginator, courcePaginator
from education.tasks import update_lesson


# CRUD на вьюсетах
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = course.objects.all()
    pagination_class = courcePaginator
    

# CRUD на дженериках
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated]

    '''
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
    '''

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()
    pagination_class = lessonPaginator

class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()
    permission_classes = [IsCurator]
    
    def perform_update(self, serializer):
        current_lesson = serializer.save()
        update_lesson.delay(current_lesson.id, 'lesson')
        #new_lesson.owner = self.request.user
        #new_lesson.save()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = lesson.objects.all()
