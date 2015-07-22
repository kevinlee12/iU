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

# All things entry related
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
def entries(request, activity_id):
    """Function to satify the gathering of entries for a particular activity"""
    try:
        activity = Activity.objects.get(id=activity_id)
        if activity.student.email != request.user.email:
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
def entry_form(request, activity_id, entry_type, entry_pk=None):
    """Function that allows the user to add/edit entries"""
    curr_student = Student.objects.get(email=request.user.email)
    activity = Activity.objects.get(id=activity_id)

    e = None
    if entry_pk:
        e = Entry.objects.get(pk=entry_pk)
        entry_verification(curr_student, e)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=e)
        if form.is_valid():
            f = form.save(commit=False)
            f.correct_entry_type()
            if type(e) == Entry:  # Editing
                f.save()
                form.save()
            else:  # New
                f.stu_email = curr_student.email
                f.activity_pk = activity.pk
                f.entry_type = entry_type
                f.save()
                form.save()
                activity.entries.add(f)
        return HttpResponseRedirect('/activity/' + activity_id)
    else:
        form = EntryForm(instance=e)

    return render(request, 'journal/entry_form.html',
                  {'form': form, 'activity': activity,
                   'entry_type': entry_type, 'entry_pk': entry_pk,
                   'entry': e})


@login_required
def delete_entry(request, activity_id, entry_pk):
    activity = get_object_or_404(Activity, id=activity_id)
    entry = get_object_or_404(Entry, pk=entry_pk)
    if entry.entry_type == "i":  # If image exists, delete it
        entry.image_entry.delete()
    activity.entries.remove(entry)
    student = Student.objects.get(email=request.user.email)
    entry_verification(student, entry)
    entry.delete()
    return HttpResponseRedirect('/activity/' + activity_id)
