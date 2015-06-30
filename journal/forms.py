from django.forms import ModelForm
from journal.models import Activity, ActivityOptions, LearningObjectiveOptions
from django.forms.widgets import CheckboxSelectMultiple


class ActivityForm(ModelForm):
    """Form for adding Activities"""

    class Meta:
        model = Activity
        fields = ['activity_name', 'activity_description', 'activity_type',
                  'learned_objective']

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.fields['activity_type'].widget = CheckboxSelectMultiple()
        self.fields['activity_type'].queryset = ActivityOptions.objects.all()
        self.fields['activity_type'].required = True

        self.fields['learned_objective'].widget = CheckboxSelectMultiple()
        self.fields['learned_objective'].queryset = LearningObjectiveOptions.objects.all()
