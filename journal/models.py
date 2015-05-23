from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    student_email = models.EmailField()
    school_id = models.IntegerField(max_length=6)
    student_id = models.IntegerField(max_length=4)
    personal_code = models.CharField(max_length=7)
