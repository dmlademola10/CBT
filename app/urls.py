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
    path('courses/', views.courses, name="courses"),
    # path('run/', views.runn, name="run"),

    # ajax
    path('exams/create/', ajax.create_exam),
    path('exams/refresh/', ajax.refresh_exam),
    path('exams/get/<str:id>', ajax.get_exam),
    path('exams/edit/', ajax.edit_exam),
    path('exams/delete/<str:id>', ajax.del_exam),
]
