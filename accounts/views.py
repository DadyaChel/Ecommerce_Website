from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
