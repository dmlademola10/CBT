"""_summary_
"""

from django.urls import path

from app import ajax
from . import views


urlpatterns = [
    path('', views.redirect, name="redirect"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('exams/', views.exams, name="exams"),
    path('faculties/', views.faculties, name="faculties"),
    path('courses/', views.courses, name="courses"),
    # path('run/', views.runn, name="run"),

    # ajax
    # exams
    path('exams/fetch/create/', ajax.create_exam),
    path('exams/fetch/refresh/', ajax.refresh_exam),
    path('exams/fetch/get/<str:id>', ajax.get_exam),
    path('exams/fetch/edit/', ajax.edit_exam),
    path('exams/fetch/delete/<str:id>', ajax.del_exam),
    # faculties
    path('faculties/fetch/create/', ajax.create_faculty),
    path('faculties/fetch/refresh/', ajax.refresh_faculty),
    path('faculties/fetch/get/<str:id>', ajax.get_faculty),
    path('faculties/fetch/edit/', ajax.edit_faculty),
    path('faculties/fetch/delete/<str:id>', ajax.del_faculty),
]
