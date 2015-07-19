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

# For all of the areas where user would first encounter
from django.shortcuts import render
from django.http import HttpResponseRedirect

from journal.models import Coordinator, Users, Student, Activity
from journal.forms import StudentRegistrationForm

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required


def coordinator(request):
    user = request.user
    students = []
    if user.is_authenticated():
        try:
            auth_user_type = Users.objects.get(email=user.email).user_type
        except ObjectDoesNotExist:
            auth_user_type = None
            return HttpResponseRedirect('/')
        if auth_user_type == 'C':
            coor = Coordinator.objects.get(email=user.email)
            students = coor.students.all().order_by('last_name')
    return render(request, 'journal/coordinator.html',
                  {'students': students, 'coordinator': coor})


@login_required
def student_registration(request, student_pk=None):
    curr_coordinator = Coordinator.objects.get(email=request.user.email)
    s = None
    if student_pk:
        s = Student.objects.get(pk=student_pk)
        if s.stu_coordinator != curr_coordinator.pk:
            return render(request, 'journal/error.html')
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=s)
        if form.is_valid():
            if type(s) == Student:
                form.save()
            else:
                f = form.save(commit=False)
                f.school = curr_coordinator.school
                f.stu_coordinator = curr_coordinator.pk
                form.save()
                f.save()
            return HttpResponseRedirect('/students')
    else:
        form = StudentRegistrationForm(instance=s)

    return render(request, 'journal/student_registration_form.html',
                  {'form': form, 'coordinator': curr_coordinator})

def coordinator_check(request, student):
    """Used for ensuring that coordinators are matched with the right students"""
    curr_coordinator = Coordinator.objects.get(email=request.user.email)
    if student.stu_coordinator != curr_coordinator != curr_coordinator.pk:
        return render(request, 'journal/error.html')
    return  # Check is good


@login_required
def student_activities(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    # coordinator_check(request, student)
    stored_activities = Activity.objects.all().filter(student=student)\
        .order_by('activity_name').reverse()
    return render(request, 'journal/activities.html',
                  {'activities': stored_activities, 'student_pk': student.pk,
                   'is_student': False})


@login_required
def student_entries(request, student_pk, activity_pk):
    student = Student.objects.get(pk=student_pk)
    coordinator_check(request, student)
    activity = Activity.objects.get(pk=activity_pk)
    activity_entries = activity.entries.all().order_by('created').reverse()
    name = activity.activity_name
    return render(request, 'journal/entries.html',
                  {'name': name, 'entries': activity_entries,
                   'activity_description': activity.activity_description,
                   'activity_pk': activity.pk, 'activity_id': activity.id,
                   'activity_start': activity.start_date,
                   'activity_end': activity.end_date or "Ongoing",
                   'is_student': False})