from rest_framework.viewsets import ModelViewSet

from curs.models import Course
from curs.serializers.courses import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()