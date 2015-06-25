from django.shortcuts import render

from journal.models import Student, Coordinator, Advisor, Users, Entry, Activity, School

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist


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


def cabinet(request):
    activities = ['No Activities!']
    if not request.user.is_anonymous():
        try:
            user_type = Users.objects.get(email=request.user.email)
        except ObjectDoesNotExist:
            user_type = None
            msg = 'User %s not found!' % request.user.get_full_name()
            activities = [msg]
        if user_type == 'S':
            try:
                student = Student.objects.get(email=request.user.email)
                activities = Activity.objects.all().filter(student=student)\
                    .order_by('last_modified').reverse()
            except ObjectDoesNotExist:
                msg = 'No Activities for %s!' % request.user.get_full_name()
                activities = [msg]
    return render(request, 'journal/cabinet.html',
                  {'activities': activities})
