from django.db import models


class Users(models.Model):
    USER_TYPES = (
        ('S', 'Student'),
        ('C', 'Coordinator'),
    )
    email = models.EmailField()
    user_type = models.CharField(max_length=1, choices=USER_TYPES)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    school_code = models.IntegerField(999999, 0)  # Max number of digits is 6

    class Meta:
        abstract = True

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def user_email(self):
        return self.email


class Student(Person):
    student_id = models.IntegerField(9999, 0)  # Max number of digits is 4
    personal_code = models.CharField(max_length=7)


class Coordinator(Person):
    coordinator_id = models.IntegerField(9999, 0)  # Max number of digits is 4


class School(models.Model):
    name = models.CharField(max_length=30, default="default")


class Entry(models.Model):
    ENTRY_TYPES = (
        ('T', 'Text'),
        ('I', 'Image'),
        ('V', 'Video'),
        ('L', 'Link'),
    )

    email = models.EmailField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=1, choices=ENTRY_TYPES)
    if entry_type == 'T':
        entry = models.TextField()
    elif entry_type == 'I':
        entry = models.ImageField()
    elif entry_type == 'V':
        entry = models.URLField()  # Web links to Youtube or else where
    else:
        entry = models.URLField()  # Web links to Youtube or else where

    def __str__(self):
        return str(self.last_modified) + ' : ' + self.entry
