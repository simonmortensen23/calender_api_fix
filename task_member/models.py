from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

class TaskMember(models.Model):
    class Access(models.TextChoices):    
        OWNER = 'OWNER', 'Owner',
        MEMBER = 'MEMBER', 'Member',

    task = models.ForeignKey('calender.CalenderPost', blank=True, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='task_members')
    access_level = models.CharField(max_length=20, choices=Access.choices, default=Access.MEMBER)

    class Meta:
        unique_together = ['task', 'user']

    def __str__(self):
        return str(self.user) 


