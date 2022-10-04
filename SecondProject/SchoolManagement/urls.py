from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/<int:pk>/',views.view_student,name='view_student'),
    path('student_create/',views.create_student,name='create_student'),
    path('student_update/<int:pk>/',views.update_student,name='update_student'),
    path('student_delete/<int:pk>/',views.delete_student,name='delete_student')
]