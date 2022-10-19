from rest_framework import serializers
from calender.models import CalenderPost
from django.contrib.humanize.templatetags.humanize import naturaltime

class CalenderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)


    class Meta:
        model = CalenderPost
        fields = [
            'id', 'owner', 'is_owner', 'created_at',
            'updated_at', 'title', 'task_info', 'due_date', 'status'
        ]