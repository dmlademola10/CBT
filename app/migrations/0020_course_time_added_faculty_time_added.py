# Generated by Django 5.0.6 on 2024-08-17 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_exam_exam_end_remove_exam_exam_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 8, 17, 22, 8, 29, 6078)),
            preserve_default=False,
        ),
    ]
