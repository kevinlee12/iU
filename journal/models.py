from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_email = models.EmailField()
    school_id = models.IntegerField(999999, 0)  # Max number of digits is 6
    student_id = models.IntegerField(9999, 0)  # Max number of digits is 4
    personal_code = models.CharField(max_length=7)

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class School(models.Model):
    name = models.CharField(max_length=30)
