from rest_framework import serializers

from curs.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
        ]
