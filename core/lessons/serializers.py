from rest_framework import serializers

from .models import Lesson
from clients.models import Subject


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ('teacher',
                  'subject',
                  'date',
                  'start_time',
                  'end_time',
                  'topic',
                  'comment',
                  'homework')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = 'title'
