# TODO: Cleaning up this mess:
from django.shortcuts import render
from django.http import HttpResponseRedirect

from journal.models import Student, Coordinator, Advisor, Users, Entry, Activity, School
from .forms import ActivityForm

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'journal/home.html',
                  {'request': request, 'user': request.user})


def welcome(request):
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


def activities(request):
    stored_activities = ['Welcome to the activities page!',
                         'You will need to be logged in to continue.']
    user = request.user
    if user.is_authenticated():
        try:
            auth_user_type = Users.objects.get(email=user.email).user_type
        except ObjectDoesNotExist:
            auth_user_type = None
            msg = 'User %s not found!' % user.get_full_name()
            stored_activities = [msg]
        if auth_user_type == 'S':
            student = Student.objects.get(email=user.email)
            stored_activities = Activity.objects.all().filter(student=student)\
                .order_by('activity_name').reverse()
            if len(stored_activities) == 0:
                msg = 'No Activities for %s!' % user.get_full_name()
                stored_activities = [msg]
    return render(request, 'journal/activities.html',
                  {'activities': stored_activities})


@login_required
def activity_form(request):
    curr_student = Student.objects.get(email=request.user.email)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.student = curr_student
            f.save()
            return HttpResponseRedirect('/cabinet')
    else:
        form = ActivityForm()

    return render(request, 'journal/activity_form.html',
                  {'form': form, 'student': curr_student.full_name()})
