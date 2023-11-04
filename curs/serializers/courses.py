from rest_framework import serializers

from curs.models import Course
from curs.serializers.lessons import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    # присваивание значения метода
    lessons_count = serializers.SerializerMethodField()
    # импорт отображения урока из серриализатора урока
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    # создание метода получения количества уроков
    def get_lessons_count(self, instance):
        return instance.lessons.count()
    