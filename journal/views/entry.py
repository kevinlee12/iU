# All things entry related
from django.shortcuts import render
from django.http import HttpResponseRedirect

from journal.models import Student, Activity, Entry
from journal.forms import EntryForm

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required


@login_required
def entries(request, activity_id):
    """Function to satify the gathering of entries for a particular activity"""
    try:
        activity = Activity.objects.get(id=activity_id)
        name = activity.activity_name
        activity_entries = activity.entries.all().order_by('last_modified')\
                                                 .reverse()
    except ObjectDoesNotExist:
        return render(request, 'journal/error.html')
    return render(request, 'journal/entries.html',
                  {'name': name, 'entries': activity_entries,
                   'activity_id': activity.id})


@login_required
def entry_form(request, activity_id, entry_pk=None):
    """Function that allows the user to add/edit entries"""
    curr_student = Student.objects.get(email=request.user.email)
    activity = Activity.objects.get(id=activity_id)
    e = None
    if entry_pk:
        e = Entry.objects.get(pk=entry_pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=e)
        if form.is_valid():
            if type(e) == Entry:
                form.save()
            else:
                f = form.save(commit=False)
                f.stu_email = curr_student.email
                f.activity_name = activity.activity_name
                f.save()
                activity.entries.add(f)
            return HttpResponseRedirect('/activity/' + activity_id)
    else:
        form = EntryForm(instance=e)

    return render(request, 'journal/entry_form.html',
                  {'form': form, 'activity': activity.activity_name})
