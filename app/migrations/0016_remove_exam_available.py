# Generated by Django 5.0.6 on 2024-06-24 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='available',
        ),
    ]
