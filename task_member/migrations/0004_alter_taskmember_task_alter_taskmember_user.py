# Generated by Django 4.1.2 on 2022-11-27 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calender', '0007_alter_calenderpost_due_date'),
        ('task_member', '0003_alter_taskmember_task_alter_taskmember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmember',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='calender.calenderpost'),
        ),
        migrations.AlterField(
            model_name='taskmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
