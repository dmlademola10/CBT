# Generated by Django 5.0.6 on 2024-06-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_exam_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='name',
        ),
        migrations.AddField(
            model_name='exam',
            name='label',
            field=models.CharField(default='kkk', max_length=100, unique=True, verbose_name='Exam Label'),
            preserve_default=False,
        ),
    ]
