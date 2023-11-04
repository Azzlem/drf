from rest_framework import serializers

from curs.models import Lessons


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
