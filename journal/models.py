from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    student_email = models.EmailField()
    school_id = models.IntegerField()
    student_id = models.IntegerField()
