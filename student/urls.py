from django.urls import path
from . import views


# app_name = 'student'

urlpatterns = [
    path('student_list/' , views.student_list, name='student_list'),
    path('add_student/' , views.add_student_with_parent, name='add_student'),
]
