from django.db import models

# The following models are used for gathering user data and storing the
# associated information of the users including journal entries and basic
# information.


class Users(models.Model):
    """For use to check if user is registered and type
    (Student or Coordinator)."""
    USER_TYPES = (
        ('S', 'Student'),
        ('C', 'Coordinator'),
        ('A', 'Advisor'),
    )
    email = models.EmailField()
    user_type = models.CharField(max_length=1, choices=USER_TYPES)

    def type_of_user(self):
        return self.user_type


class School(models.Model):
    """School object"""
    school_code = models.CharField(max_length=6)  # Max number of digits is 6
    school_name = models.CharField(max_length=30)


class Person(models.Model):
    """Abstract class for all individuals"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    school = models.ForeignKey(School)

    class Meta:
        abstract = True

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def user_email(self):
        return self.email


class Coordinator(Person):
    """Coordinator object that inherits from Person"""


class Advisor(Person):
    """Advisor object that inherits from Person"""


class Student(Person):
    """Student object that inherits from Person"""
    student_id = models.CharField(max_length=4)  # Max number of digits is 4
    personal_code = models.CharField(max_length=7)
    coordinator = models.ForeignKey(Coordinator)
    advisor = models.ForeignKey(Advisor)


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
