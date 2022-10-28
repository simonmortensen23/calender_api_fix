from django.db import IntegrityError
from rest_framework import serializers
from .models import TaskMember
from django.contrib.auth.models import User

class MemberSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = ['username']


class TaskMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMember
        fields = ['user', 'task', 'access_level']


class ChangeTaskMemberShipSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(max_length=50, min_length=1, allow_blank=False, source='task_member.user.username')

    class Meta:
        model = TaskMember
        fields = ['username', 'task']


