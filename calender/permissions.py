from rest_framework import permissions
from task_member.models import TaskMember

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # get user's membership
        memberships = TaskMember.objects.filter(user=request.user, task=obj)

        # if no membership at all, return False
        if len(memberships) != 1:
            return False
        else:
            # if membership exists, return True if access_level is OWNER
            return memberships[0].access_level == TaskMember.Access.OWNER


class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return True only if user is in task.members
        return request.user in obj.members.all()
