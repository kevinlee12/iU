from django.shortcuts import render

from journal.models import Student, Coordinator, Users, Entry

from datetime import datetime


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
    try:
        entries = Entry.objects.all().filter(email=request.user.email)\
            .order_by('last_modified').reverse()
    except ObjectDoesNotExist:
        entries = None
    return render(request, 'journal/cabinet.html', 
                  {})
