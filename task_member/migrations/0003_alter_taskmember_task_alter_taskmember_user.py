# Generated by Django 4.1.2 on 2022-11-26 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0006_calenderpost_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_member', '0002_taskmember_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmember',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='calender.calenderpost'),
        ),
        migrations.AlterField(
            model_name='taskmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
