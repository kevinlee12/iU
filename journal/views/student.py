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

from journal.models import Student, Activity
from journal.forms import ActivityForm

from journal.models import Entry
from journal.forms import EntryForm

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from .utilities import unread_notifications_count


def profile(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'journal/student_profile.html', {'student': student})


def stu_activities(request):
    """Function for the main activities page"""
    stored_activities = []
    user = request.user
    is_student = False
    if user.is_authenticated():
        try:
            student = Student.objects.get(user=user)
            stored_activities = Activity.objects.filter(student=student)\
                .order_by('activity_name').reverse()
        except ObjectDoesNotExist:
            return render(request, 'journal/404.html')
            student = None
            stored_activities = []
        is_student = True
    return render(request, 'journal/activities.html',
                  {'activities': stored_activities, 'is_student': is_student})


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
                action.send(curr_student, verb='modifed the activity',
                            target=a, seen=False)
                return HttpResponseRedirect('/activity/{0}'.format(a.pk))
            else:
                f = form.save(commit=False)
                f.student = curr_student
                f.save()
                form.save()
                action.send(curr_student, verb='created a new activity',
                            target=a, seen=False)
                return HttpResponseRedirect('/activities')
    else:
        form = ActivityForm(instance=a)

    return render(request, 'journal/activity_form.html',
                  {'form': form, 'student': curr_student, 'activity': a})


@login_required
def activity_deletion(request, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    student_activity_check(request, activity)
    entries = activity.entries.all()
    for entry in entries:
        delete_entry(request, activity.id, entry.pk)
    activity.delete()
    return HttpResponseRedirect('/activities/')


def entry_verification(student, entry):
    if student.pk != entry.stu_pk:
        return Http404()


@login_required
def stu_entries(request, activity_pk):
    """Function to satify the gathering of entries for a particular activity"""
    try:
        activity = Activity.objects.get(pk=activity_pk)
        if activity.student.user.email != request.user.email:
            # Redirect its not the corresponding activity
            return HttpResponseRedirect('/activities')
        name = activity.activity_name
        activity_entries = activity.entries.order_by('created').reverse()
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/activities')
    return render(request, 'journal/entries.html',
                  {'name': name, 'entries': activity_entries,
                   'activity_description': activity.activity_description,
                   'activity_pk': activity_pk,
                   'activity_start': activity.start_date,
                   'activity_end': activity.end_date or 'Ongoing',
                   'is_student': True})


@login_required
def entry_form(request, activity_pk, entry_pk=None):
    """Function that allows the user to add/edit entries"""
    curr_student = Student.objects.get(user=request.user)
    activity = Activity.objects.get(pk=activity_pk)

    e = None
    if entry_pk:
        e = Entry.objects.get(pk=entry_pk)
        entry_verification(curr_student, e)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=e)
        if form.is_valid():
            f = form.save(commit=False)
            if type(e) == Entry:  # Editing
                f.save()
                form.save()
                action.send(curr_student, verb='edited an entry of',
                            target=activity, seen=False)
            else:  # New
                f.stu_pk = curr_student.pk
                f.activity_pk = activity.pk
                f.save()
                form.save()
                activity.entries.add(f)
                action.send(curr_student, verb='added an entry in',
                            target=activity, seen=False)
        return HttpResponseRedirect('/entries/' + activity_pk)
    else:
        form = EntryForm(instance=e)

    return render(request, 'journal/entry_form.html',
                  {'form': form, 'activity': activity,
                   'entry_pk': entry_pk, 'entry': e})


@login_required
def delete_entry(request, activity_pk, entry_pk):
    activity = get_object_or_404(Activity, pk=activity_pk)
    entry = get_object_or_404(Entry, pk=entry_pk)
    activity.entries.remove(entry)
    student = Student.objects.get(user=request.user)
    entry_verification(student, entry)
    entry.delete()
    return HttpResponseRedirect('/entries/' + str(activity_pk))
