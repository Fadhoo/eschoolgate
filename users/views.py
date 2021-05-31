from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import StudentSerializer, UserSerializer, UserDetailSerializer
from .models import User, Profile


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfile(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = StudentSerializer
    queryset = Profile.objects.all()
