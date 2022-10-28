from django.db import models
from django.contrib.auth.models import User
from task_member.models import TaskMember
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class CalenderPost(models.Model):

    class TaskStatus(models.TextChoices):    
        IN_PROGRESS = 'A', 'In progress',
        IDLE = 'B', 'Idle',
        DONE = 'C', 'Done'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    task_info = models.TextField(blank=True)
    due_date = models.DateTimeField()
    task_status = models.CharField(max_length=1, choices=TaskStatus.choices, default=TaskStatus.IDLE)
    members = models.ManyToManyField(User, through=TaskMember)

    def validate_date(due_date):
        if due_date < timezone.now():
            raise ValidationError("Date cannot be in the past")
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        validators=[validate_date]
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


