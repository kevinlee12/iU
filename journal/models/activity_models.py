# coding: utf-8
#
# Copyright 2015 The iU Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    activity_description = models.TextField(max_length=150)

    activity_type = models.ManyToManyField(ActivityOptions)
    learned_objective = models.ManyToManyField(LearningObjectiveOptions)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

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

    def shorten(word, max_length):
        if len(word) > max_length:
            new_str = word[:max_length]
            new_str += '...'
            return new_str
        return word

    def name_short(self):
        return Activity.shorten(self.activity_name, 18)

    def description_short(self):
        return Activity.shorten(self.activity_description, 70)
