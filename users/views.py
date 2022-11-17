import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User, Location
from django_Avito.serializers import UserCreateModelSerializer, UserModelSerializer, UserUpdateModelSerializer, \
    UserDeleteModelSerializer


class Users_List_View(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class Users_Detail_View(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class Users_Create_View(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer

class Users_Update_View(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateModelSerializer

class Users_Delete_View(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteModelSerializer


