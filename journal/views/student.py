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

# For all things activity related (with the exception of entries) for students.
from actstream import action
from actstream.models import user_stream
from actstream.models import following

from django.shortcuts import render
from django.http import HttpResponseRedirect

from journal.models import Student, UserType, Activity
from journal.forms import ActivityForm

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from .entry import delete_entry


def stu_activities(request):
    """Function for the main activities page, login is not required"""
    stored_activities = []
    user = request.user
    is_student = False
    if user.is_authenticated():
        try:
            auth_user_type = UserType.objects.get(user=request.user).user_type
        except ObjectDoesNotExist:
            auth_user_type = None
            msg = 'User {0} not found!'.format(user.get_full_name())
            stored_activities = [msg]
        if auth_user_type == 'S':
            student = Student.objects.get(user=user)
            stored_activities = Activity.objects.all().filter(student=student)\
                .order_by('activity_name').reverse()
            is_student = True
    return render(request, 'journal/activities.html',
                  {'activities': stored_activities, 'is_student': is_student,
                   'feed': user_stream(request.user)})


def student_activity_check(request, activity):
    curr_student = Student.objects.get(user=request.user)
    if activity.student != curr_student:
        return render(request, 'journal/error.html')
    return


@login_required
def activity_form(request, activity_pk=None):
    curr_student = Student.objects.get(user=request.user)
    a = None
    if activity_pk:
        a = Activity.objects.get(pk=activity_pk)
        student_activity_check(request, a)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=a)
        if form.is_valid():
            if type(a) == Activity:
                form.save()
                action.send(curr_student, verb='modifed the activity', target=a)
                return HttpResponseRedirect('/activity/' + str(a.id))
            else:
                f = form.save(commit=False)
                f.student = curr_student
                f.save()
                form.save()
                action.send(curr_student, verb='created a new activity', target=a)
                return HttpResponseRedirect('/activities')
    else:
        form = ActivityForm(instance=a)

    return render(request, 'journal/activity_form.html',
                  {'form': form, 'student': curr_student,
                   'activity': a})


@login_required
def activity_deletion(request, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    student_activity_check(request, activity)
    entries = activity.entries.all()
    for entry in entries:
        delete_entry(request, activity.id, entry.pk)
    activity.delete()
    return HttpResponseRedirect('/activities/')
