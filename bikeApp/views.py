from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import permissions
from bikeApp.serializers import UserSerializer, GroupSerializer

from rest_framework.viewsets import ModelViewSet
# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
