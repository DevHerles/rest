from django.shortcuts import render
from profiles.models import Profiles
from rest_framework import viewsets
from .serializers import ProfilesSerializer


class ProfileList(viewsets.ModelViewSet):
    serializer_class = ProfilesSerializer
    queryset = Profiles.objects.all()
