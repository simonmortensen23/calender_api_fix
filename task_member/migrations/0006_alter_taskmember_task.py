# Generated by Django 4.1.2 on 2022-11-27 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0007_alter_calenderpost_due_date'),
        ('task_member', '0005_alter_taskmember_task_alter_taskmember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmember',
            name='task',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='calender.calenderpost'),
        ),
    ]