from rest_framework import serializers

from curs.models import Course, Lessons


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
        ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = [
            'title',
            'description',
            'url',
        ]
