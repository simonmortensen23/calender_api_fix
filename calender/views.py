from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from calender_api.permissions import IsOwnerOrReadOnly, IsOwner
from .models import CalenderPost
from .serializers import CalenderSerializer


# Create your views here.
class CalenderList(generics.ListCreateAPIView):
    serializer_class = CalenderSerializer
    permission_classes = [IsOwner]
    queryset = CalenderPost.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CalenderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CalenderSerializer
    queryset = CalenderPost.objects.all().order_by('-created_at')