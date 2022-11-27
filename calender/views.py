from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from calender_api.permissions import IsAuthenticated
from .permissions import IsMember, IsOwner
from .models import CalenderPost
from .serializers import CalenderSerializer
from task_member.models import TaskMember
from task_member.serializers import ChangeTaskMemberShipSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
import time
from rest_framework import serializers

# Create your views here.
class CalenderList(generics.ListCreateAPIView):
    serializer_class = CalenderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # retrieve user from session
        user = self.request.user

        # retrieve all tasks where user is member
        tasks = CalenderPost.objects.filter(
            members__in=[user]
        ).order_by('-created_at')

        # return tasks
        return tasks


    def perform_create(self, serializer):
        # find user from request
        user = self.request.user

        # ensure user is not anonymous
        if user.id is None:
            return serializer.ValidationError('You are not authorized')

        # save new task
        task = serializer.save()

        # add owner membership between new task and user
        task_member = TaskMember(
            access_level=TaskMember.Access.OWNER,
            user=user,
            task=task
        )
        task_member.save()




class CalenderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CalenderSerializer
    queryset = CalenderPost.objects.all().order_by('-created_at')

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsMember]
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()


class AddTaskMember(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ChangeTaskMemberShipSerializer
    queryset = CalenderPost.objects.all()
    allowed_methods = ['POST']

    def perform_create(self, serializer):
        username = serializer.data['username']
        task_id = self.kwargs['pk']

        # small timeout (avoid username detection by primitive bots)
        time.sleep(0.2)

        # retrieve task_id
        task = CalenderPost.objects.filter(id=task_id).first()
        if task is None:
            # TODO: return some kind of 404 error
            raise serializers.ValidationError('Task does not exist')

        # retrieve user from request (by provided username)
        user = User.objects.filter(username=username).first()
        if user is None:
            # TODO: return some kind of 400 error
            raise serializers.ValidationError('Unable to add member, because user does not exist')
        

        # ensure user not task member
        if user in task.members.all():
            raise serializers.ValidationError('Unable to add member, because user is already member')


        # add user as task member
        new_membership = TaskMember(task=task, user=user)
        new_membership.save()

        return JsonResponse({"success": True})


class DeleteTaskMember(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ChangeTaskMemberShipSerializer
    queryset = CalenderPost.objects.all()
    allowed_methods = ['POST']

    def create(self, instance, pk):
        username = self.request.data.get('username')

        # small timeout (avoid username detection by primitive bots)
        time.sleep(0.2)

        # retrieve user from request (by provided username)
        user = User.objects.filter(username=username).first()
        if user is None:
            # TODO: return some kind of 400 error
            raise serializers.ValidationError('Unable to remove member, because user does not exist')

        # retrieve task_id
        task = CalenderPost.objects.filter(id=pk).first()
        if task is None:
            # TODO: return some kind of 404 error
            raise serializers.ValidationError('Task does not exist')
        
        # find membership and ensure it's existence
        membership = TaskMember.objects.filter(task=task, user=user).first()
        if membership is None:
            raise serializers.ValidationError('Unable to remove member, because user is not member')
        
        # delete membership
        membership.delete()

        return JsonResponse({"success": True})
