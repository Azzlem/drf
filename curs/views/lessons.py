from rest_framework import generics

from curs.models import Lessons
from curs.serializers.lessons import LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lessons.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lessons.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lessons.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
