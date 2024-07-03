# Generated by Django 5.0.6 on 2024-06-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_exam_name_exam_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='done',
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.CharField(default='', max_length=50, verbose_name='Course'),
            preserve_default=False,
        ),
    ]
