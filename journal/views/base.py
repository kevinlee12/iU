# For all of the areas where user would first encounter

from django.shortcuts import render

from datetime import datetime


def home(request):
    """Function to satisfy the home page"""
    return render(request, 'journal/home.html',
                  {'request': request, 'user': request.user})


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
