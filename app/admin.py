from django.contrib import admin
from app import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Course)
admin.site.register(models.Faculty)
admin.site.register(models.Exam)
