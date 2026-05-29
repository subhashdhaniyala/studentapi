from django.db import models

# Create your models here.

'''Model: Student
Fields:
- name (short text)
- email (short text)
- course (short text)
- grade (short text)
- enrolled_on (date — auto set on creation)
- is_active (boolean — default True)'''

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    course=models.CharField(max_length=100)
    grade=models.CharField(max_length=2)
    enrolled_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
