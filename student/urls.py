from django.urls import path
from . import views


# app_name = 'student'

urlpatterns = [
    path('add_student/' , views.add_student_with_parent, name='add_student'),
    path('student_list/' , views.student_list, name='student_list'),
    path('student_detail/<slug:slug>' , views.student_detail, name='student_detail'),
    path('delete_student/<slug:slug>' , views.delete_student, name='delete_student'),
    path('edit_student/<slug:slug>' , views.edit_student, name='edit_student'),
]
