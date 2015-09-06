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

# For all of the areas where user would first encounter
from actstream import action
from actstream.models import user_stream
from django.contrib.auth.models import User

from .student import stu_activities, activity_form
from .coordinator import activities_view, activity_view

from .student import stu_entries, entry_form
from .coordinator import entries_view, view_stu_entry

from django.http import HttpResponseRedirect
from django.shortcuts import render

from journal.models import Coordinator, Student, Advisor
from journal.models import Activity, Entry

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from journal.forms import ContactForm

import itertools


def home(request):
    """Function to satisfy the home page"""
    if request.user and not request.user.is_anonymous:
        return HttpResponseRedirect('/activities/')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']  # TODO: Change recipients
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'journal/home.html',
                  {'request': request, 'user': request.user, 'form': form})


def get_user_type(request):
    """Grabs the user type via the permissions in auth.User"""
    return User.objects.get(email=request.user.email)\
        .user_permissions.all()[0].codename

def gateway(request):
    return


def login_redirects(request):
    """Function that redirects users appropriately after login"""
    try:
        user_type = get_user_type(request)
    except:
        return HttpResponseRedirect('/')
    if user_type == 'stu':
        return HttpResponseRedirect('/activities')
    elif user_type == 'coor':
        return HttpResponseRedirect('/coordinator')
    elif user_type == 'advise':
        return HttpResponseRedirect('/advise')
    return HttpResponseRedirect('/')


def feed(request):
    """Grabs all of the feeds for the user"""
    return render(request, 'journal/feed.html',
                  {'feed': user_stream(request.user)})

# The following functions redirect call the appropriate function based on
# the user is a student, coordinator, or advisor.


@login_required
def activities(request, student_pk=None):
    """Grabs all the activities associated with the student"""
    user_type = get_user_type(request)

    if user_type == 'stu':
        return stu_activities(request)
    elif user_type == 'coor' or user_type == 'advise':
        return activities_view(request, student_pk)
    return


@login_required
def activity_details(request, activity_pk=None):
    """Grabs the activity details (for staff) or form for the student"""
    user_type = get_user_type(request)

    if user_type == 'stu':
        return activity_form(request, activity_pk)
    elif user_type == 'coor' or user_type == 'advise':
        return activity_view(request, activity_pk)


@login_required
def entries(request, activity_pk):
    """Grabs all of the entries associated with the activity"""
    user_type = get_user_type(request)

    if user_type == 'stu':
        return stu_entries(request, activity_pk)
    elif user_type == 'coor' or user_type == 'advise':
        return entries_view(request, activity_pk)


@login_required
def entry(request, activity_pk, entry_pk=None):
    """Grabs the entry or entry form if the user is a student."""
    user_type = get_user_type(request)

    if user_type == 'stu':
        return entry_form(request, activity_pk, entry_pk)
    elif user_type == 'coor' or user_type == 'advise':
        return view_stu_entry(request, activity_pk, entry_pk)


@login_required
def comment_submit(request):
    """Notifies all associated parties of the user when he or she comments."""
    url_source = request.META['HTTP_REFERER']
    user_type = get_user_type(request)
    if user_type == 'stu':
        user = Student.objects.get(user=request.user)
    elif user_type == 'coor':
        user = Coordinator.objects.get(user=request.user)
    elif user_type == 'advise':
        user = Advisor.objects.get(user=request.user)
    url_source = url_source.split("/")
    if 'entry' in url_source:
        source = Entry.objects.get(pk=url_source[-2])
        action.send(user, verb='commented on an entry in', target=source,
                    seen=False)
    elif 'activity_details' in url_source:
        source = Activity.objects.get(pk=url_source[-1])
        action.send(user, verb='commented on', target=source, seen=False)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
