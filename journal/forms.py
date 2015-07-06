from django.forms import ModelForm
from journal.models import Activity, ActivityOptions, LearningObjectiveOptions
from journal.models import Entry
from django.forms.widgets import CheckboxSelectMultiple

from django import forms

import datetime


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
                  'activity_adviser', 'advisor_phone', 'advisor_phone']

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.fields['activity_type'].widget = CheckboxSelectMultiple()
        self.fields['activity_type'].queryset = ActivityOptions.objects.all()
        self.fields['activity_type'].required = True

        self.fields['learned_objective'].widget = CheckboxSelectMultiple()
        self.fields['learned_objective'].queryset = LearningObjectiveOptions.objects.all()


class EntryForm(ModelForm):
    """Form for adding Entries for Activity"""

    class Meta:
        model = Entry
        fields = ['entry_type', 'entry']
