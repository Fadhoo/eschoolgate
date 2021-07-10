from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .serializers import SubjectSerializer, LessonSerializer
from .models import Subject, Lesson


class SubjectList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectDetails(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class LessonList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
