# Generated by Django 4.1.2 on 2022-10-25 12:11

import calender.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calenderpost',
            name='due_date',
            field=models.DateTimeField(validators=[calender.models.CalenderPost.validate_date]),
        ),
    ]
