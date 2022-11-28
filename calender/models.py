from django.db import models
from django.contrib.auth.models import User
from task_member.models import TaskMember
from datetime import date
from django.core.exceptions import ValidationError


# Create your models here.
class CalenderPost(models.Model):

    class TaskStatus(models.TextChoices):    
        IN_PROGRESS = 'IN PROGRESS', 'In progress',
        IDLE = 'IDLE', 'Idle',
        DONE = 'DONE', 'Done'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    task_info = models.TextField(blank=True)
    task_status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.IDLE)
    members = models.ManyToManyField(User, through=TaskMember)

    def validate_date(due_date):
        if due_date < date.today():
            raise ValidationError("Date cannot be in the past")
    due_date = models.DateField(
        validators=[validate_date]
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


