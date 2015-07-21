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

# TODO: Split this file

from django.forms import ModelForm
from journal.models import Activity, ActivityOptions, LearningObjectiveOptions
from journal.models import Entry
from journal.models import Student
from journal.models import Advisor
from django.forms.widgets import CheckboxSelectMultiple

from django import forms

import datetime


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=300, widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class AdvisorForm(ModelForm):
    """Form for handling advisors"""

    class Meta:
        model = Advisor
        fields = ['first_name', 'last_name', 'email']


class StudentRegistrationForm(ModelForm):
    """Form for handling student registration"""

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'student_id',
                  'personal_code']


class ActivityForm(ModelForm):
    """Form for adding Activities"""

    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(required=False)
    activity_adviser = forms.CharField(required=False)
    advisor_email = forms.CharField(required=False)
    advisor_phone = forms.CharField(required=False)

    class Meta:
        model = Activity
        fields = ['activity_name', 'activity_description', 'activity_type',
                  'learned_objective', 'start_date', 'end_date',
                  'activity_adviser', 'advisor_phone', 'advisor_email']

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.fields['activity_type'].widget = CheckboxSelectMultiple()
        self.fields['activity_type'].queryset = ActivityOptions.objects.all()
        self.fields['activity_type'].required = True

        self.fields['learned_objective'].widget = CheckboxSelectMultiple()
        self.fields['learned_objective'].queryset = LearningObjectiveOptions\
            .objects.all()


class EntryForm(ModelForm):
    """Form for adding Entries for Activity"""

    class Meta:
        model = Entry
        fields = ['text_entry', 'image_entry', 'link_entry']
