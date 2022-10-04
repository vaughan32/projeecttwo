from django.db import models

class Student(models.Model):
    student_number = models.CharField(max_length=5)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    field_of_study = models.CharField(max_length=15)
    gpa = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
