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
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

    STATUS = (
        ('N', 'New'),
        ('A', 'Active'),
        ('I', 'Inactive'),  # This is for deleted users queued for removal
    )
    email = models.EmailField()
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    # status = models.CharField(max_length=1, choices=STATUS)

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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def user_email(self):
        return self.email


class Student(Person):
    """Student object that inherits from Person"""
    student_id = models.CharField(max_length=4)  # Max number of digits is 4
    personal_code = models.CharField(max_length=7)
    # For the following, please use the respective pk fields.
    stu_coordinator = models.IntegerField()

    def get_absolute_url(self):
        return '/student_activities/{0}/'.format(self.pk)

class IBAdmin(Person):
    students = models.ManyToManyField(Student, blank=True)

    class Meta:
        abstract = True


class Advisor(IBAdmin):
    """Advisor object that inherits from Person"""


class Coordinator(IBAdmin):
    """Coordinator object that inherits from Person"""
    advisors = models.ManyToManyField(Advisor)
