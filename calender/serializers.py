from rest_framework import serializers
from calender.models import CalenderPost
from task_member.models import TaskMember
from task_member.serializers import MemberSerializer, TaskMemberSerializer
from django.contrib.humanize.templatetags.humanize import naturaltime


class CalenderSerializer(serializers.ModelSerializer):
    membership = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    members = MemberSerializer(read_only=True, many=True)


    def get_membership(self, obj):
        request = self.context['request']
        
        # get member ship of user
        my_memberships = TaskMember.objects.filter(
            task=obj,
            user=request.user
        )

        # do some error handling
        if len(my_memberships) != 1:
            print("User has zero or more memberships!")
            # TODO: raise some kind of HTTPError statuscode 401
            return {'value': None, 'human': 'Unknown'}
        else:
            # return access level from user's membership
            value = my_memberships[0].access_level
            human = my_memberships[0].get_access_level_display()
            return {
                'value': value,
                'human': human
            }

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)


    class Meta:
        model = CalenderPost
        fields = [
            'id', 'membership', 'created_at', 'members',
            'updated_at', 'title', 'task_info', 'due_date', 'task_status'
        ]