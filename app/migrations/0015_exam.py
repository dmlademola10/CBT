# Generated by Django 5.0.6 on 2024-06-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Exam Code')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Exam Name')),
                ('available', models.BooleanField(default=False, verbose_name='Exam available to be written')),
                ('exam_start', models.DateTimeField(null=True, verbose_name='Exam be available at')),
                ('exam_end', models.DateTimeField(null=True, verbose_name='Exam be unavailable at')),
                ('done', models.BooleanField(default=False, verbose_name='Exam done')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
