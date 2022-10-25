from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CalenderPost(models.Model):

    IN_PROGRESS = 'in progress'
    IDLE = 'idle'
    DONE = 'done'

    TASK_STATUS = (
        (IN_PROGRESS, 'In progress'),
        (IDLE, 'Idle'),
        (DONE, 'done')
    )
    def validate_date(due_date):
        if due_date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    task_info = models.TextField(blank=True)
    due_date = models.DateTimeField(validators=[validate_date])
    status = models.CharField(max_length=20, choices=TASK_STATUS, default=IN_PROGRESS)

    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


