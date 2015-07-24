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

# All things entry related
from actstream import action

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from journal.models import Student, Activity, Entry
from journal.forms import EntryForm

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404


def entry_verification(student, entry):
    if student.email != entry.stu_email:
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
        activity_entries = activity.entries.all().order_by('created').reverse()
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/activities')
    return render(request, 'journal/entries.html',
                  {'name': name, 'entries': activity_entries,
                   'activity_description': activity.activity_description,
                   'activity_pk': activity.pk, 'activity_id': activity.id,
                   'activity_start': activity.start_date,
                   'activity_end': activity.end_date or 'Ongoing',
                   'is_student': True})


@login_required
def entry_form(request, activity_pk, entry_pk=None):
    """Function that allows the user to add/edit entries"""
    curr_student = Student.objects.get(user=request.user)
    activity = Activity.objects.get(pk=activity_pk)

    e = None
    entry_type = 'text'
    if entry_pk:
        e = Entry.objects.get(pk=entry_pk)
        entry_type = e.entry_type
        entry_verification(curr_student, e)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=e)
        if form.is_valid():
            f = form.save(commit=False)
            f.correct_entry_type()
            if type(e) == Entry:  # Editing
                f.save()
                form.save()
                action.send(curr_student, verb='added an entry to', target=activity)
            else:  # New
                f.stu_email = curr_student.email
                f.activity_pk = activity.pk
                f.save()
                form.save()
                activity.entries.add(f)
                action.send(curr_student, verb='edited an entry of', target=activity)
        return HttpResponseRedirect('/entries/' + activity_pk)
    else:
        form = EntryForm(instance=e)

    return render(request, 'journal/entry_form.html',
                  {'form': form, 'activity': activity,
                   'entry_type': entry_type, 'entry_pk': entry_pk,
                   'entry': e})


@login_required
def delete_entry(request, activity_pk, entry_pk):
    activity = get_object_or_404(Activity, pk=activity_pk)
    entry = get_object_or_404(Entry, pk=entry_pk)
    if entry.entry_type == "i":  # If image exists, delete it
        entry.image_entry.delete()
    activity.entries.remove(entry)
    student = Student.objects.get(user=request.user)
    entry_verification(student, entry)
    entry.delete()
    return HttpResponseRedirect('/entries/' + str(activity_pk))
