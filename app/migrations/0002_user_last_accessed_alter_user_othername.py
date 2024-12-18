# Generated by Django 5.0.6 on 2024-06-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_accessed',
            field=models.DateTimeField(null=True, verbose_name='Last Seen'),
        ),
        migrations.AlterField(
            model_name='user',
            name='othername',
            field=models.CharField(blank=True, max_length=100, verbose_name='Full Name'),
        ),
    ]
