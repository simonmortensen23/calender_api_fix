from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class CalenderPost(models.Model):

    
    TASK_STATUS = (
        (IN_PROGRESS, 'In progress'),
        (IDLE, 'Idle'),
        (DONE, 'done')
    )
   


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    task_info = models.TextField(blank=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=TASK_STATUS)

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


