from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UserCreateSerializer

USER_MODEL = get_user_model()


class UserCreateView(CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserCreateSerializer


# class ProfileView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = USER_MODEL.objects.all()
#
#     def get_object(self):
#         return self.request.user


class UserDetailView(RetrieveAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer

