from django.shortcuts import render

from datetime import datetime


def index(request):
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


def diary(request):
    return render(request, 'journal/diary.html')
