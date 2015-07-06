from django.db import models

from .users_models import *

# The following are used for activity and entry logging.

class Entry(models.Model):
    """Entry object used for journaling"""
    ENTRY_TYPES = (
        ('T', 'Text'),
        ('I', 'Image'),
        ('V', 'Video'),
        ('L', 'Link'),
    )
    stu_email = models.EmailField()
    activity_name = models.CharField(max_length=30)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=1, choices=ENTRY_TYPES)
    entry = models.TextField()
    # if entry_type == 'T':
    #     entry = models.TextField()
    # elif entry_type == 'I':
    #     entry = models.ImageField()
    # elif entry_type == 'V':
    #     entry = models.URLField()  # Web links to Youtube or else where
    # elif entry_type == 'L':
    #     entry = models.URLField()  # Web links to Youtube or else where

    def __str__(self):
        return str(self.last_modified) + ' : ' + self.entry


class ActivityOptions(models.Model):
    """Activity Option objects used for Activity Objects
       Note: The options must be loaded in order for the forms to work!
    """

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class LearningObjectiveOptions(models.Model):
    """Learning Objective objects used for Activity Objects
       Note: The options must be loaded in order for the forms to work!
    """

    objective = models.CharField(max_length=70)

    def __str__(self):
        return self.objective

class Activity(models.Model):
    """Activites for the students, depends on ActivityOptions
       and LearningObjectiveOptions to be preloaded
    """
    student = models.ForeignKey(Student)

    activity_name = models.CharField(max_length=30)
    activity_description = models.CharField(max_length=150)

    activity_type = models.ManyToManyField(ActivityOptions)
    learned_objective = models.ManyToManyField(LearningObjectiveOptions)

    entries = models.ManyToManyField(Entry, blank=True)

    def __str__(self):
        return self.activity_name
