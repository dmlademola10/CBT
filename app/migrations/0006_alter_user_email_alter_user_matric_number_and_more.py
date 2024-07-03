# Generated by Django 5.0.6 on 2024-06-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='matric_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Matriculation Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.PositiveBigIntegerField(unique=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Username'),
        ),
    ]
