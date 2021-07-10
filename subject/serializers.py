from rest_framework import serializers
from .models import Lesson, Subject


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Subject
        fields = ('name', 'classroom', 'lesson',)


class SubjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
