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
from actstream.actions import follow, unfollow
from actstream.models import user_stream
from actstream.models import following

from django.shortcuts import render
from django.http import HttpResponseRedirect

from journal.models import Coordinator, Student, Advisor
from journal.models import Activity, Entry
from journal.forms import StudentRegistrationForm, AdvisorForm

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Permission


try:
    STUDENT_PERM = Permission.objects.get(codename='stu')
    ADVISOR_PERM = Permission.objects.get(codename='advise')
except:
    STUDENT_PERM = None
    ADVISOR_PERM = None


def coordinator(request):
    coor = Coordinator.objects.get(user=request.user)
    students = coor.students.all().order_by('last_name')
    advisors = coor.advisors.all().order_by('first_name')
    if not following(request.user):
        for student in students:
            follow(request.user, student)
            follow(User.objects.get(email=student.user.email), coor)

    return render(request, 'journal/coordinator.html',
                  {'feed': user_stream(request.user), 'students': students,
                   'coordinator': coor, 'advisors': advisors})


def advisor(request):
    advisor = Advisor.objects.get(user=request.user)
    students = advisor.students.all().order_by('last_name')
    for student in students:
        follow(request.user, student)
        follow(User.objects.get(email=student.user.email), advisor)

    return render(request, 'journal/advisor.html',
                  {'feed': user_stream(request.user), 'students': students})


def user_creation(email, user_type):
    exists = User.objects.filter(email=email).count()
    if not exists:
        User.objects.create(email=email, user_type=user_type)
    return


def user_removal(email):
    exists = User.objects.filter(email=email).count()
    if exists:
        User.objects.get(email=email).delete()
    return


def is_student(request):
    return User.objects.get(email=request.user.email)\
        .user_permissions.filter(codename='stu').exists()


@login_required
def advisors_form(request, advisor_pk=None):
    curr_coordinator = Coordinator.objects.get(user=request.user)

    advisor = None
    if advisor_pk:
        advisor = Advisor.objects.get(pk=advisor_pk)

    if request.method == 'POST':
        form = AdvisorForm(request.POST, instance=advisor, coor=curr_coordinator)
        if form.is_valid():
            if type(advisor) == Advisor:
                form.save()
            else:
                f = form.save(commit=False)
                f.school = curr_coordinator.school
                # Create user in django auth
                advisor_email = form.cleaned_data['email']
                try:
                    new_advisor = User.objects\
                        .create_user(advisor_email, advisor_email)
                except IntegrityError:
                    new_advisor = User.objects.get(email=advisor_email)
                new_advisor.user_permissions.add(ADVISOR_PERM)
                f.user = new_advisor
                f.save()
                form.save()
                curr_coordinator.advisors.add(f)
                follow(request.user, f)
                follow(new_advisor, curr_coordinator)
            return HttpResponseRedirect('/coordinator')
    else:
        form = AdvisorForm(instance=advisor, coor=curr_coordinator)
    return render(request, 'journal/advisor_registration.html',
                  {'form': form, 'coordinator': curr_coordinator})


def get_user_type(request):
    return User.objects.get(email=request.user.email)\
        .user_permissions.all()[0].codename


def staff_check(request, student):
    """Used for ensuring that coordinators are matched with the right
       students
    """
    staff_type = get_user_type(request)
    if staff_type == 'coor':
        staff = Coordinator.objects.get(user=request.user)
    elif staff_type == 'advise':
        staff = Advisor.objects.get(user=request.user)
    if student not in staff.students.all():
        return render(request, 'journal/error.html')
    return  # Check is good


@login_required
def student_registration(request, student_pk=None):
    # TODO: Allow advisors to register students
    curr_coordinator = Coordinator.objects.get(user=request.user)

    s = None
    if student_pk:
        s = Student.objects.get(pk=student_pk)
        staff_check(request, s)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=s)
        if form.is_valid():
            if type(s) == Student:
                form.save()
            else:
                f = form.save(commit=False)
                f.school = curr_coordinator.school
                f.stu_coordinator = curr_coordinator.pk
                # Create user in django auth
                stu_email = form.cleaned_data['email']
                try:
                    new_stu = User.objects.create_user(stu_email, stu_email)
                except IntegrityError:
                    new_stu = User.objects.get(email=stu_email)
                new_stu.user_permissions.add(STUDENT_PERM)
                f.user = new_stu
                form.save()
                f.save()
                curr_coordinator.students.add(f)
                follow(request.user, f)
                follow(new_stu, curr_coordinator)
            return HttpResponseRedirect('/coordinator')
    else:
        form = StudentRegistrationForm(instance=s)

    return render(request, 'journal/student_registration_form.html',
                  {'form': form, 'coordinator': curr_coordinator,
                   'student_pk': student_pk})


def delete_stu_entry(activity_id, entry_pk):
    activity = get_object_or_404(Activity, id=activity_id)
    entry = get_object_or_404(Entry, pk=entry_pk)
    activity.entries.remove(entry)
    entry.delete()
    return


def activity_stu_deletion(activity):
    entries = activity.entries.all()
    for entry in entries:
        delete_entry(activity.id, entry.pk)
    activity.delete()
    return


@login_required
def remove_student(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    staff_check(request, student)
    stu = User.objects.get(email=student.user.email)
    try:
        unfollow(request.user, student)
        unfollow(stu, request.user)
    except:
        pass
    student.delete()
    return HttpResponseRedirect('/coordinator')


@login_required
def activities_view(request, student_pk):
    """For viewing all activities related to the student"""
    student = Student.objects.get(pk=student_pk)
    staff_check(request, student)
    stored_activities = Activity.objects.all().filter(student=student)\
        .order_by('activity_name').reverse()
    staff_type = get_user_type(request)
    if staff_type == 'coor':
        back_link = 'coordinator'
    else:
        back_link = 'advise'
    return render(request, 'journal/activities.html',
                  {'activities': stored_activities, 'student_pk': student.pk,
                   'is_student': False, 'back_link': back_link})


@login_required
def activity_view(request, activity_pk):
    """For viewing specific activity specifics"""
    activity = Activity.objects.get(pk=activity_pk)
    staff_check(request, activity.student)
    return render(request, 'journal/activity_description_coor_view.html',
                  {'student': activity.student, 'activity': activity})


@login_required
def entries_view(request, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    student = activity.student
    staff_check(request, student)
    activity_entries = activity.entries.all().order_by('created').reverse()
    name = activity.activity_name
    return render(request, 'journal/entries.html',
                  {'name': name, 'entries': activity_entries,
                   'activity_description': activity.activity_description,
                   'activity_pk': activity.pk, 'activity_id': activity.id,
                   'activity_start': activity.start_date,
                   'activity_end': activity.end_date or "Ongoing",
                   'student_pk': student.pk,
                   'is_student': False})


@login_required
def view_stu_entry(request, activity_pk, entry_pk):
    staff_type = get_user_type(request)
    if staff_type == 'coor':
        staff = Coordinator.objects.get(user=request.user)
    elif staff_type == 'advise':
        staff = Advisor.objects.get(user=request.user)
    activity = Activity.objects.get(pk=activity_pk)
    entry = Entry.objects.get(pk=entry_pk)
    student = activity.student
    staff_check(request, student)
    return render(request, 'journal/entry_coor_view.html',
                  {'entry': entry, 'activity': activity,
                   'coordinator': staff})
