from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from calender_api.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from profiles.serializers import ProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()