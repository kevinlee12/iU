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
from actstream import action

from journal.models import Users, Student, Advisor, Coordinator
from journal.models import Entry, Activity

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail

from journal.forms import ContactForm


def home(request):
    """Function to satisfy the home page"""
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


def login_redirects(request):
    """Function that redirects users appropriately after login"""
    try:
        user = Users.objects.get(email=request.user.email)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/activities')
    if user.user_type == 'S':
        return HttpResponseRedirect('/activities')
    elif user.user_type == 'C':
        return HttpResponseRedirect('/coordinator')
    return home(request)


@login_required
def comment_ping(request):
    referer = str(request.META['HTTP_REFERER'])
    referer = referer.split('/')

    def entry_extract(location):
        entry_pk = str(referer[location])
        return Entry.objects.get(pk=entry_pk)

    def activity_extract(location):
        activity_pk = str(referer[location])
        return Activity.objects.get(pk=activity_pk)

    if 'entry_form' in referer:
        obj = entry_extract(-2)
    elif 'entry_view' in referer:
        obj = entry_extract(-2)
    elif 'activity' in referer:
        obj = activity_extract(-1)

    user = get_object_or_404(Users, email=request.user.email)
    if user.user_type == 'S':
        user = Student.objects.get(email=user.email)
    elif user.user_type == 'C':
        user = Coordinator.objects.get(email=user.email)
    action.send(user, verb='commented on', target=obj)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
