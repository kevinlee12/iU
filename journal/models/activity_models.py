from django.db import models
from django.core.validators import RegexValidator

from .entry_models import Entry
from .users_models import Student

# The following contains the Activity model along with the supporting models:
# - ActivityOptions: Creativity, Action, and Service (from fixtures)
# - LearningObjectiveOptions: 7 learning objects (from fixtures)


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

    start_date = models.DateField()
    end_date = models.DateField(auto_now_add=True, blank=True, null=True)

    activity_adviser = models.CharField(max_length=50)
    advisor_email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: \
                                '+999999999'. Up to 15 digits allowed.")
    advisor_phone = models.CharField(blank=True, null=True,
                                     validators=[phone_regex], max_length=15)

    entries = models.ManyToManyField(Entry, blank=True)

    def __str__(self):
        return self.activity_name
