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
from django.http import HttpResponseRedirect
from django.shortcuts import render

from journal.models import Users

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail

from journal.forms import ContactForm 

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

            recipients = ['info@example.com']
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
        return HttpResponseRedirect('/students')
    return home(request)


def welcome(request):
    """For the landing page after the user logs in"""
    name = ''
    current_hour = datetime.now().time().hour
    if current_hour < 12:
        greeting = 'Good morning'
    elif current_hour < 17:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    if request.user.is_authenticated():
        name = ' ' + request.user.get_full_name()
    return render(request, 'journal/welcome.html',
                  {'name': name, 'greeting': greeting})
