# Generated by Django 5.0.6 on 2024-06-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_user_suspended'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Exam Code')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Exam Name')),
                ('available', models.BooleanField(default=False, verbose_name='Exam available to be written')),
                ('done', models.BooleanField(default=False, verbose_name='Exam done')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='last_accessed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
